import { Animal } from "./Animal";

export class Gato extends Animal {
    constructor(protected nombre: string) {
        super(nombre);
    }

    hacerSonido(): void {
        console.log(`${this.nombre} hacer Mauuuu`)
    }
}