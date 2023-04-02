import { Car } from "./Car";
import { Customer } from "./Customer";

export interface Sales{
    id:number;
    car_id: Car;
    customer_id: Customer;
    date: Date;
    name_of_dealer: string;
    price: number;
    
}