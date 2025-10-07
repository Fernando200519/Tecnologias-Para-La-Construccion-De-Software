import { Gato } from "./animals/Gato";
import { Paloma } from "./animals/Paloma";
import { Pato } from "./animals/Pato";

const paloma = new Paloma("La Paloma");
paloma.hacerSonido()
paloma.volar()
paloma.dormir()
console.log("{----------------}")

const gato = new Gato("El Gato")
gato.hacerSonido()
gato.dormir()
console.log(gato.getNombre)

const pato = new Pato("El Pato")
pato.hacerSonido()
pato.volar()
pato.nadar()