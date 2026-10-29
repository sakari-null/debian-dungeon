import random

def read_high_score():
    record_name = None
    record_hp = -1

    try:
        with open("highscore.txt", "r") as file:
            current_record = file.read().strip()
            parts = current_record.split()
            record_name = parts[0].rstrip(":")
            record_hp = int(parts[1])
    except FileNotFoundError:
        pass

    return record_name, record_hp


def start_game():

    while True:
        print("\n---- Welcome to the Debian Dungeon ----")
        record_name, record_hp = read_high_score()

        if record_name is not None:
            print(f"Current Record Holder -> {record_name}: {record_hp} HP")
        else:
            print("Current Record Holder -> No scores recorded yet! Be the first.")
            print("---------------------------------")

        player_name = input("Enter your hero's name: ")

        health = 100
        inventory = ["torch"]

        print(f"\nWelcome, {player_name}! HP: {health} | Inventory: {inventory}")
        print("You enter dark corridor and scary Terminal Bug block's your way.")

        choice1 = input("Do you FIGHT or RUN away? (fight/run): ").lower()

        if choice1 == "fight":
            damage = random.randint(10, 40)
            health = health - damage
            print(f"Current HP: {health}")

            print("You found a 'health_potion' on the floor! Added to inventory.")
            inventory.append("health_potion")

        elif choice1 == "run":
            print("\nYou safely trip over a rock but escape into the next room.")
        else:
            print("\nYou hesitated. The bug nipped your ankles for 5 damage.")
            health = health - 5

        print(f"\nMoving on... HP: {health} | Inventory: {inventory}")
        print("You reach a dark, locked chest. It requires a torch to inspect safely.")

        if "torch" in inventory:
            choice2 = input("Use your torch to open the chest? (yes/no):").lower()
            if choice2 == "yes" and "health_potion" in inventory:
                print("\nYou safely open chest, drink your health potion, and find the golden Debian source code! YOU WIN!")
                if health > record_hp:
                    print(f"Saving your high score of {health} HP...")
                    with open("highscore.txt", "w") as file:
                        file.write(f"{player_name}: {health} HP")
                else:
                    print("You won, but the old high score remains!")
            elif choice2 == "yes":
                print("\nYou open the chest but it's a trap! Exploded. Game over!.")
            else:
                print("\nYou walked past the chest and left the dungeon safely.")
        else:
            print("\nWithout a torch, you stumble in the dark, break your neck and die. Game over!")

        print("\n==========================================")
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing the Debian Dungeon! Goodbye.")
            break


start_game()

