import { Animal } from "./Animal";
import { Volar } from "../skills/Volar";

export class Paloma extends Animal implements Volar{
    constructor(public nombre: string){
        super(nombre);
    }

    hacerSonido(): void {
        console.log(`${this.nombre} hacer Brrrr`)
    }

    volar(): void {
        console.log(`${this.nombre} estoy volando`)
    }
}