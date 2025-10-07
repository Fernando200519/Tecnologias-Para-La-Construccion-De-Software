import { Animal } from "./Animal";
import { Volar } from "../skills/Volar";

export class Pato extends Animal implements Volar{
    constructor(public nombre: string){
        super(nombre);
    }

    hacerSonido(): void {
        console.log(`${this.nombre} hace Cuaaakk`)
    }

    volar(): void {
        console.log(`${this.nombre} `)
    }

}
