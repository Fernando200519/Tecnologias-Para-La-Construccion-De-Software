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
    return new UserProfile(
      this.name,
      this.email,
      this.address,
      this.preferences
    );
  }
}

const original = new UserProfile(
  "Ana",
  "ana@example.com",
  { street: "Av. 1", city: "Coatzacoalcos" },
  { theme: "dark", notifications: true }
);

const copy = original.clone();
copy.preferences.theme = "light";
console.log("original prefs:", original.preferences);
