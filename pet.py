class Pet:
    """Імітує життя домашнього улюбленця (кіт або собака)."""

    SOUNDS = {"кіт": "Няв!", "собака": "Гав!"}

    def __init__(self, name, kind="собака"):
        if kind not in self.SOUNDS:
            raise ValueError("Вид має бути 'кіт' або 'собака'")
        self.name = name
        self.kind = kind
        self.hunger = 50      # 0 - ситий, 100 - дуже голодний
        self.energy = 50      # 0 - виснажений, 100 - повний сил
        self.mood = 50        # 0 - сумний, 100 - щасливий
        self.alive = True

    def _limit(self):
        """Тримає показники в межах 0..100 та перевіряє, чи улюбленець живий."""
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.mood = max(0, min(100, self.mood))
        if self.hunger >= 100 and self.energy <= 0:
            self.alive = False

    def _check_alive(self):
        if not self.alive:
            print(f"{self.name} більше не з нами...")
        return self.alive

    def eat(self):
        if not self._check_alive():
            return
        self.hunger -= 30
        self.energy += 10
        self.mood += 10
        print(f"{self.name} смачно поїв(ла).")
        self._limit()

    def play(self):
        if not self._check_alive():
            return
        if self.energy < 20:
            print(f"{self.name} надто втомлений(а), щоб гратися.")
            return
        self.energy -= 20
        self.hunger += 15
        self.mood += 25
        action = "ганяє м'яч" if self.kind == "собака" else "полює на мишку-іграшку"
        print(f"{self.name} {action}!")
        self._limit()

    def sleep(self):
        if not self._check_alive():
            return
        self.energy += 40
        self.hunger += 10
        print(f"{self.name} солодко спить... Zzz")
        self._limit()

    def speak(self):
        if not self._check_alive():
            return
        print(f"{self.name}: {self.SOUNDS[self.kind]}")
        self.mood += 5
        self._limit()

    def status(self):
        state = "живий" if self.alive else "помер"
        print(f"[{self.kind} {self.name}] {state} | "
              f"голод: {self.hunger} | енергія: {self.energy} | настрій: {self.mood}")


if __name__ == "__main__":
    pet = Pet("Барсик", "кіт")
    pet.status()
    pet.speak()
    pet.play()
    pet.eat()
    pet.sleep()
    pet.status()
