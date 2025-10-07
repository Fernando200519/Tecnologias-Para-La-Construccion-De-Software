import { PaymentService } from "./services/PayMentService";
import { PayPalPayMent } from "./models/PayPalPayMent";
import { BitCoinPayMent } from "./models/BitCoinPayMent";
import { CreditPayMent } from "./models/CreditCardPayMent";

const service = new PaymentService();

const creditCard = new CreditPayMent();

const payPal = new PayPalPayMent();

const bitcoin = new BitCoinPayMent();

service.serviceProcess(creditCard, 200);
service.serviceProcess(payPal, 500);
service.serviceProcess(bitcoin, 1000);