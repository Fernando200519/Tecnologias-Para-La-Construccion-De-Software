class Tv {
  powerOn() {
    console.log("📺 TV encendida");
  }
  powerOff() {
    console.log("📺 TV apagada");
  }
}

class Radio {
  powerOn() {
    console.log("📻 Radio encendida");
  }
  powerOff() {
    console.log("📻 Radio apagada");
  }
}

class TvRemote {
  constructor(private tv: Tv) {}
  turnOn() {
    this.tv.powerOn();
  }
}

class RadioRemote {
  constructor(private radio: Radio) {}
  turnOn() {
    this.radio.powerOn();
  }
}

const tvRemote = new TvRemote(new Tv());
tvRemote.turnOn();
