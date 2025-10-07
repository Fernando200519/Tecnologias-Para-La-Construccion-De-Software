import { PayMentMethod } from "./PayMentMethod";

export class PayPalPayMent extends PayMentMethod{
    pay(amount){
        console.log("Pago procesado por PayPal $" + amount)
    }
}