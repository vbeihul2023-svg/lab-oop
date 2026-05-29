from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass


class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return (
            f"⚔️  Удар мечем '{self.name}' — {current_attack} шкоди. "
            f"У '{another_item.name}' залишилось HP: {another_item.health}"
        )

    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp} одиниць"

    def sharpening(self):
        self._sharp += 1
        print(f"🔪 Меч '{self.name}' заточено! Бонус гостроти: +{self._sharp}")


class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return (
            f"🪓 Удар сокирою '{self.name}' — {current_attack} шкоди. "
            f"У '{another_item.name}' залишилось HP: {another_item.health}"
        )

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp} одиниць"


class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int = 5):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return (
            f"🏹 Постріл луком '{self.name}' — {current_attack} шкоди. "
            f"У '{another_item.name}' залишилось HP: {another_item.health}"
        )

    @property
    def get_attack_power(self):
        return (
            f"Атака лука {self.name}: "
            f"{self.__attack_power + self.range_power} одиниць"
        )

    def reload(self):
        self.range_power += 1
        print(f"🎯 Лук '{self.name}' перезаряджено! Дальність: {self.range_power}")


def choose_weapon(player_num):
    weapons = {
        "1": Sword(f"Ескалібур-{player_num}", 80),
        "2": Axe(f"Кратос-{player_num}", 75),
        "3": Bow(f"Аполлон-{player_num}", 70),
    }
    print(f"\nГравець {player_num}, обери зброю:")
    print("  1 — ⚔️  Меч (атака + заточення)")
    print("  2 — 🪓 Сокира (важкий удар)")
    print("  3 — 🏹 Лук (атака + перезарядка)")
    while True:
        choice_input = input("Твій вибір (1/2/3): ").strip()
        if choice_input in weapons:
            return weapons[choice_input]
        print("Невірний вибір, спробуй ще раз.")


def player_turn(attacker, defender):
    print(f"\n--- Хід гравця: '{attacker.name}' ---")
    print(f"  HP твоєї зброї: {attacker.health}")
    print(f"  HP суперника '{defender.name}': {defender.health}")

    actions = {"1": "Атакувати"}
    print("  1 — ⚔️  Атакувати")

    if isinstance(attacker, Sword):
        actions["2"] = "Заточити меч"
        print("  2 — 🔪 Заточити меч (+гострота)")
    elif isinstance(attacker, Bow):
        actions["2"] = "Перезарядити лук"
        print("  2 — 🎯 Перезарядити лук (+дальність)")

    while True:
        action = input("Твоя дія: ").strip()
        if action in actions:
            break
        print("Невірна дія, спробуй ще раз.")

    if action == "1":
        print(attacker.attack(defender))
    elif action == "2":
        if isinstance(attacker, Sword):
            attacker.sharpening()
        elif isinstance(attacker, Bow):
            attacker.reload()


def bot_turn(attacker, defender):
    print(f"\n--- Хід бота: '{attacker.name}' ---")
    action = choice(["attack", "boost"])

    if action == "boost" and isinstance(attacker, Sword):
        attacker.sharpening()
    elif action == "boost" and isinstance(attacker, Bow):
        attacker.reload()
    else:
        print(attacker.attack(defender))


def main():
    print("=" * 50)
    print("       ⚔️  ПОКРОКОВА ГРА ⚔️")
    print("=" * 50)

    mode = input("\nОбери режим:\n  1 — Гравець vs Бот\n  2 — Гравець vs Гравець\nВибір: ").strip()

    weapon1 = choose_weapon(1)

    if mode == "2":
        weapon2 = choose_weapon(2)
        two_players = True
    else:
        weapons_list = [
            Sword("Темний меч", 85),
            Axe("Берсерк", 90),
            Bow("Тінь", 75),
        ]
        weapon2 = choice(weapons_list)
        two_players = False
        print(f"\n🤖 Бот обрав: {weapon2.name}")

    print("\n" + "=" * 50)
    print(f"  {weapon1.name}  ⚔️  VS  ⚔️  {weapon2.name}")
    print("=" * 50)

    turn = 0
    while True:
        turn += 1
        print(f"\n{'='*50}\n🎮 ХІД {turn}")

        player_turn(weapon1, weapon2)
        if weapon2.health <= 0:
            print(f"\n🏆 Перемога '{weapon1.name}'!")
            break

        if two_players:
            player_turn(weapon2, weapon1)
        else:
            bot_turn(weapon2, weapon1)

        if weapon1.health <= 0:
            print(f"\n🏆 Перемога '{weapon2.name}'!")
            break


if __name__ == "__main__":
    main()
