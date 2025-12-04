// good-prototype.ts
type Address = { street: string; city: string };
type Preferences = { theme: string; notifications: boolean };

class UserProfile {
  constructor(
    public name: string,
    public email: string,
    public address: Address,
    public preferences: Preferences
  ) {}

  clone(): UserProfile {
    const addressCopy: Address = { ...this.address };
    const prefsCopy: Preferences = { ...this.preferences };
    return new UserProfile(this.name, this.email, addressCopy, prefsCopy);
  }

  cloneUsingStructuredClone(): UserProfile {
    const deep =
      typeof structuredClone === "function"
        ? structuredClone({
            name: this.name,
            email: this.email,
            address: this.address,
            preferences: this.preferences,
          })
        : {
            name: this.name,
            email: this.email,
            address: { ...this.address },
            preferences: { ...this.preferences },
          };
    return new UserProfile(
      deep.name,
      deep.email,
      deep.address,
      deep.preferences
    );
  }
}

// Prueba demostrativa
const original = new UserProfile(
  "Ana",
  "ana@example.com",
  { street: "Av. 1", city: "Coatzacoalcos" },
  { theme: "dark", notifications: true }
);

const safeCopy = original.clone();
safeCopy.preferences.theme = "light";

console.log("original prefs:", original.preferences);
console.log("copy prefs:", safeCopy.preferences);
