export abstract class Animal {
    constructor(protected nombre: string) {

        
    }

    abstract hacerSonido(): void;

    dormir(): void {
        console.log(`${this.nombre} esta durmiendo` )
    }

    getNombre(): string {
        return this.nombre
    }
}