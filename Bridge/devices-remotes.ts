interface Device {
  turnOn(): void;
  turnOff(): void;
  setVolume?(value: number): void;
}

class Tv implements Device {
  turnOn() {
    console.log("TV encendida");
  }
  turnOff() {
    console.log("TV apagada");
  }
  setVolume(v: number) {
    console.log(`TV volumen: ${v}`);
  }
}

class Radio implements Device {
  turnOn() {
    console.log("Radio encendida");
  }
  turnOff() {
    console.log("Radio apagada");
  }
  setVolume(v: number) {
    console.log(`Radio volumen: ${v}`);
  }
}

class RemoteControl {
  constructor(protected device: Device) {}

  turnOn() {
    this.device.turnOn();
  }
  turnOff() {
    this.device.turnOff();
  }
}

class AdvancedRemote extends RemoteControl {
  mute() {
    console.log("Silencio activado");
    this.device.setVolume?.(0);
  }
}

const tvRemote = new AdvancedRemote(new Tv());
tvRemote.turnOn();
tvRemote.mute();

const radioRemote = new AdvancedRemote(new Radio());
radioRemote.turnOn();
radioRemote.mute();
