import { CarBrand } from "./CarBrand";
import { Sales } from "./Sales";
import { Customer } from "./Customer";

export interface Car
{

    id:number;
    name:CarBrand;
    description:string;
    engine:string;
    type:string;
    year:number;
    horsepower:number;
    sales:Sales[];

}