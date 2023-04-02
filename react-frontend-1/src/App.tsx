import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AllBrands } from "./components/CarBrand/AllBrands";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";
import { BrandAdd } from "./components/CarBrand/BrandAdd";
import { BrandDelete } from "./components/CarBrand/BrandDelete";
import { BrandDetails } from "./components/CarBrand/BrandDetails";
import { BrandUpdate } from "./components/CarBrand/BrandUpdate";
import { AverageProdYear } from "./components/statistics/AverageProdYear";

///
///
function App() {
	return (
		<React.Fragment>
			<Router>
				<AppMenu />

				<Routes>
					<Route path="/" element={<AppHome />} />
					<Route path="/brands" element={<AllBrands />} />
					<Route path="/brands/add" element={<BrandAdd />} />
			
					<Route path="brands/:brandId/delete" element={<BrandDelete />} />
					<Route path="brands/:brandId/details" element={<BrandDetails />} />
					<Route path="/brands/:brandId/edit" element={<BrandUpdate />} />

					<Route path="/averageprodyear" element={<AverageProdYear/>}></Route>
          {/*
          <Route path="/owners/:ownerId/edit" element={<OwnerUpdate />} />
					<Route path="/owners/:ownerId/delete" element={<OwnerDelete />} />
					<Route path="/owners/add" element={<OwnerAdd />} />
					<Route path="/averageprodyear" element={<AverageProdYear/>}></Route> */}
				</Routes>
			</Router>
		</React.Fragment>
	);
}

export default App;