export class PaymentService{
    serviceProcess(paymentMethod, amount){
        paymentMethod.pay(amount);
    }
}