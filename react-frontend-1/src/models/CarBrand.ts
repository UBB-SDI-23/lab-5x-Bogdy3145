import { Car } from "./Car";


export interface CarBrand{

    id?:number;
    name:string;
    founding_year:string;
    owner_name:string;
    rarity:string;
    hq_address:string;
    cars?:Car[];
}