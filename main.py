import random
import math

_author_ = "Garrett Dixon"


# Garrett Dixon
# this program guides the user through a number of operations in the form
# of a game
# The clutter at the top is so that the last 20 lines of code look nice

def main():
    player_hp = 100
    enemy_hp = 10
    level = 1
    gold = 0
    damage_multi = 1
    attack_loop = 0
    base_damage = 0
    upgrade1 = 1
    upgrade2 = 1
    upgrade3 = 1

    print("Welcome to the Integration Project!")
    name = input("First you have to choose a name")
    print("you have encountered an enemy")

    while attack_loop != 1:
        try:
            attack = int(input("attack it by typing 1"))
            if attack == 1:
                attack_loop = 1
                success = swing(player_hp, enemy_hp, level, damage_multi, base_damage, name)
                gold = after_battle(success, gold, level)
            else:
                print("please type 1")
                attack_loop = 0
        except:
            print("please type 1")
            attack_loop = 0

    print("Congratulations on defeating your first enemy!")
    # this line thinks is sql for some reason
    print("select the shop from the location menu")

    shop_loop = 0
    while shop_loop == 0:
        destination = location_menu()
        if destination == 0:
            shop_loop = 1
            level += 1
        elif destination == 1:
            upgrade = shop_menu(upgrade1, upgrade2, upgrade3, gold)
            if upgrade == 0:
                cost = int((200 ** math.log2(upgrade1 * 1.1)) // 1)
                gold -= cost
                upgrade1 += 1
                base_damage += 1
                print("Your Base Damage is now", base_damage)
            elif upgrade == 1:
                cost2 = 75 * (upgrade2 ** 1.002) // 1
                gold -= cost2
                upgrade2 += 1
                player_hp *= 2
                print("Your hit points is now", player_hp)
            elif upgrade == 2:
                cost3 = 1000 * (upgrade3 ** 1.001) // 1
                gold -= cost3
                upgrade3 += 1
                damage_multi += 0.02
                print("Your Damage Multiplier is now", damage_multi)
            elif upgrade == 3:
                pass
        if destination == 2:
            mini_game()
        if destination == 3:
            print("Thank you for playing")
            quit()

    # the main loop starts here
    main_loop = 0
    while main_loop == 0:
        success = swing(player_hp, enemy_hp, level, damage_multi, base_damage, name)
        gold = after_battle(success, gold, level)
        shop_loop = 0
        while shop_loop == 0:
            destination = location_menu()
            if destination == 0:
                shop_loop = 1
                level += 1
            if destination == 1:
                upgrade = shop_menu(upgrade1, upgrade2, upgrade3, gold)
                if upgrade == 0:
                    cost = int((200 ** math.log2(upgrade1 * 1.1)) // 1)
                    gold -= cost
                    upgrade1 += 1
                    base_damage += 1
                    print("Your Base Damage is now", base_damage)
                elif upgrade == 1:
                    cost = 75 * upgrade2
                    gold -= cost
                    upgrade2 += 1
                    player_hp = player_hp * 2
                    print("Your hit points is now", player_hp)
                elif upgrade == 2:
                    cost = 1000 * upgrade3
                    gold -= cost
                    upgrade3 += 1
                    damage_multi += 0.02
                    print("Your Damage Multiplier is now", damage_multi)
                elif upgrade == 3:
                    pass
            if destination == 2:
                mini_game()
            if destination == 3:
                print("Thank you for playing")
                quit()


def mini_game():
    """Prompts the player to try to guess the same number as the program"""
    mode_name = ""
    for mode in range(1, 4):
        if mode == 1:
            mode_name = "Easy"
        if mode == 2:
            mode_name = "Normal"
        if mode == 3:
            mode_name = "Impossible"
        print(mode, ".", mode_name)
    difficulty = (input("chose the difficulty"))
    # checks to make sure number entered is valid
    try:
        difficulty = int(difficulty)
    except:
        print("Invalid selection. Try again.")
        return
    if difficulty > 3:
        difficulty = int(difficulty)
        print("Invalid selection. Try again.", sep="")
        return
    if difficulty < 1:
        difficulty = int(difficulty)
        print("Invalid selection. Try again.", end="")
        return
    if difficulty == 1:
        wrong_loop = 0
        while wrong_loop == 0:
            guess = input("try to guess the same number as the computer. The"
                          " computer will guess 1 or 2")
            # checks to make sure number entered is valid
            try:
                guess = int(guess)
                if guess > 2:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess < 1:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess == 1 or 2:
                    wrong_loop = 1
                    if (guess % 2) == 0:
                        print("you chose an even number")
                    if guess == 1 or guess == 2:
                        print("You win!")

            except:
                print("Invalid selection. Try again.")
    if difficulty == 2:
        wrong_loop = 0
        while wrong_loop == 0:
            guess = input("try to guess the same number as the computer. The"
                          " computer will guess 1 or 2")
            computer_guess = random.randrange(1, 3)
            # checks to make sure number entered is valid
            try:
                guess = int(guess)
                if guess > 2:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess < 1:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess == 1 or 2:
                    wrong_loop = 1
                    if guess != (not computer_guess):
                        print("You win!")
                    else:
                        print("You Lost!")
                        print("the computer chose", computer_guess)
            except:
                print("Invalid selection. Try again.")
    if difficulty == 3:
        wrong_loop = 0
        while wrong_loop == 0:
            guess = input("try to guess the same number as the computer. The"
                          " computer will guess 1 or 2")
            # checks to make sure number entered is valid
            try:
                guess = int(guess)
                if guess > 2:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess < 1:
                    guess = int(guess)
                    print("Invalid selection. Try again.")
                if guess == 1 or 2:
                    wrong_loop = 1
                    if guess == 1 and guess == 2:
                        print("You win!")
                    else:
                        print("You Lost!")
                        print("the computer chose 11")

            except:
                print("Invalid selection. Try again.")


def shop_menu(func_upgrade1, func_upgrade2, func_upgrade3, func_gold):
    """controls the shop interface"""
    func_cost1 = int((200 ** math.log2(func_upgrade1 * 1.01)) // 1)
    func_cost2 = 75 * (func_upgrade2 ** 1.002) // 1
    func_cost3 = 1000 * (func_upgrade3 ** 1.001) // 1
    print("1. Upgrade your base damage for", func_cost1)
    print("2. Increase your base hit points for", func_cost2)
    print("3. Increase your damage multiplier for", func_cost3)
    print("4. Leave")
    print("You currently have", func_gold, "gold")
    choice = input()
    try:
        choice = int(choice)
    except:
        print("Invalid selection. Try again.")
        return 4
    if choice > 4:
        print("Invalid selection. Try again.")
        return 4
    if choice < 1:
        print("Invalid selection. Try again.")
        return 4
    if choice == 1:
        if func_gold < func_cost1:
            print("you don't have enough gold for that upgrade")
            return 4
        else:
            return 0
    if choice == 2:
        if func_gold < func_cost2:
            print("you don't have enough gold for that upgrade")
            return 4
        else:
            return 1
    if choice == 3:
        if func_gold < func_cost3:
            print("you don't have enough gold for that upgrade")
            return 4
        else:
            return 2
    if choice == 4:
        return 3


def swing(func_player_hp, func_enemy_hp, func_level, func_damage_multi,
          func_base_damage, func_name):
    """handles combat"""
    dead = 0
    func_enemy_hp = func_enemy_hp * func_level
    while not dead:
        func_enemy_hp -= (random.randrange(func_base_damage,
                                           func_base_damage + 5)
                          ** func_damage_multi) // 1
        func_player_hp -= random.randrange(0 + func_level, 2 + func_level) * \
                          func_level
        print("the enemy hp is now", func_enemy_hp)
        print(func_name + "'s hp is now", func_player_hp)
        if func_player_hp <= 0:
            return 0
        if func_enemy_hp <= 0:
            return 1

    # finds if the player won or lost the battle and responds accordingly


def after_battle(func_success, func_gold, func_level):
    """calculates gold and if the player won or lost"""
    if func_success == 1:
        print("Congratulations!")
        func_gold += random.randrange(50, 150) * func_level
        print("You defeated the enemy")
        print("You now have", func_gold, "gold")
        return func_gold
    else:
        print("Game Over!" * 10)
        print("You lost so bad that I said it 10 times!")
        quit()

    # controls the menu for locations


def location_menu():
    """
    Runs the menu regarding the players location
    """
    loc_name = ""
    for location in range(1, 5):
        if location == 1:
            loc_name = "fight"
        elif location == 2:
            loc_name = "shop"
        elif location == 3:
            loc_name = "minigame"
        elif location == 4:
            loc_name = "Quit Game"
        print(location, ".", loc_name)
    func_destination = input("chose the number where you want to go")
    try:
        func_destination = int(func_destination)
    except:
        print("Invalid selection. Try again.")
        return 5
    if func_destination > 4:
        print("Invalid selection. Try again.")
        return 5
    if func_destination < 1:
        print("Invalid selection. Try again.")
        return 5
    if func_destination == 1:
        return 0
    if func_destination == 2:
        return 1
    if func_destination == 3:
        return 2
    if func_destination == 4:
        return 3


main()
