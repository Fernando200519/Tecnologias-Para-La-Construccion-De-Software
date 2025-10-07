import { PayMentMethod } from "./PayMentMethod";

export class CreditPayMent extends PayMentMethod{
    pay(amount){
        console.log("Pagando procesado por Tarjeta de credito $" + amount)
    }
}