"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django1 import controller
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

schema_view = get_swagger_view(title='Jaseci API')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('docs/', schema_view),
    path("admin/", admin.site.urls),
    path("cars/", controller.cars_list),
    path('cars/<int:id>', controller.cars_detail),
    path('brands/', controller.brand_list),
    path('brands/<int:id>', controller.brand_detail),
    path('customers/', controller.custromer_list),
    path('customers/<int:id>', controller.customer_detail),
    path('customers/filtered/<int:year>', controller.customer_filtered),
    path('sales/', controller.sale_list),
    path('sales/<int:id>', controller.sales_detail),
    path("statistic/", controller.statistic, name="stat"),
    path("statistic/hp/", controller.statisticHp, name="stat2"),
    path("brand/assign", controller.assigning_brands_to_cars),
    path("brand/create/cars", controller.assigning_brands_to_new_cars)

]

urlpatterns = format_suffix_patterns(urlpatterns)