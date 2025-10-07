import { PayMentMethod } from "./PayMentMethod";

export class BitCoinPayMent extends PayMentMethod{
    pay(amount){
        console.log("Pago procesado por bitcoin $" + amount)
    }
}