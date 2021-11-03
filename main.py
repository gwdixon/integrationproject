import math
import random

# Garrett Dixon
# this program guides the user through a number of operations in the form
# of a game
# The clutter at the top is so that the last 20 lines of code look nice


playerHP = 100
enemyHP = 10
level = 1
gold = 0
prestige = 0
damageMulti = 1
attackLoop = 0
location = 1
baseDamage = 0
upgrade1 = 1
upgrade2 = 1
upgrade3 = 1

print("Welcome to the Integration Project!")
name = input("First you have to choose a name")
print("you have encountered an enemy")


def swing(funcplayerhp, funcenemyhp, funclevel, funcdamagemulti,
          funcbasedamage):
    dead = 0
    funcenemyhp = funcenemyhp * funclevel
    while dead == 0:
        funcenemyhp -= (random.randrange(funcbasedamage, funcbasedamage + 5) \
                       ** funcdamagemulti) // 1
        funcplayerhp -= random.randrange(0 + funclevel, 5 + funclevel) *\
                        funclevel
        print("the enemy hp is now", funcenemyhp)
        print(name + "'s hp is now", funcplayerhp)
        if funcplayerhp <= 0:
            dead = 1
            return 0
        if funcenemyhp <= 0:
            dead = 1
            return 1


def afterBattle(funcsuccess, funcgold, funclevel):
    if funcsuccess == 1:
        print("Congratulations!")
        funcgold += random.randrange(50, 150) * funclevel
        print("You defeated the enemy")
        print("You now have", funcgold, "gold")
        return funcgold
    else:
        print("Game Over!" * 10)
        print("You lost so bad that I said it 10 times!")
        quit()


while attackLoop != 1:
    try:
        attack = int(input("attack it by typing 1"))
        attackLoop = 1
        success = swing(playerHP, enemyHP, level, damageMulti, baseDamage)
    except:
        print("please type 1")
        attackLoop = 0
        attack = int(input("attack it by typing 1"))

gold = afterBattle(success, gold, level)
print("Congratulations on defeating your first enemy!")
# this line thinks is sql for some reason
print("Select the shop from the location menu")


def locationMenu():
    for location in range(1, 4):
        if location == 1:
            locName = "fight"
        if location == 2:
            locName = "shop"
        if location == 3:
            locName = "minigame"
        print(location, ".", locName)
    funcdestination = input("chose the number where you want to go")
    try:
        funcdestination = int(funcdestination)
    except:
        print("Invalid selection. Try again.")
        locationMenu()
    if funcdestination > 3:
        funcdestination = int(funcdestination)
        print("Invalid selection. Try again.")
        locationMenu()
    if funcdestination < 1:
        funcdestination = int(funcdestination)
        print("Invalid selection. Try again.")
        locationMenu()
    if funcdestination == 1:
        funcdestination = int(funcdestination)
        return 0
    if funcdestination == 2:
        funcdestination = int(funcdestination)
        return 1
    if funcdestination == 3:
        funcdestination = int(funcdestination)
        return 2


def shopMenu(funcupgrade1, funcupgrade2, funcupgrade3, funcgold):
    funccost1 = int((200 ** math.log2(funcupgrade1 * 1.01)) // 1)
    funccost2 = 75 * (funcupgrade2 ** 1.002) // 1
    funccost3 = 1000 * (funcupgrade3 ** 1.001) // 1
    print("1. Upgrade your base damage for", funccost1)
    print("2. Increase your base hit points for", funccost2)
    print("3. Increase your damage multiplier for", funccost3)
    print("4. Leave")
    print("You currently have", funcgold, "gold")
    choice = input()
    try:
        choice = int(choice)
    except:
        print("Invalid selection. Try again.")
        locationMenu()
    if choice > 4:
        print("Invalid selection. Try again.")
        locationMenu()
    if choice < 1:
        print("Invalid selection. Try again.")
        locationMenu()
    if choice == 1:
        if funcgold < funccost1:
            print("you don't have enough gold for that upgrade")
            shopMenu(upgrade1, upgrade2, upgrade3, gold)
        else:
            return 0
    if choice == 2:
        if funcgold < funccost2:
            print("you don't have enough gold for that upgrade")
            shopMenu(upgrade1, upgrade2, upgrade3, gold)
        else:
            return 1
    if choice == 3:
        if funcgold < funccost3:
            print("you don't have enough gold for that upgrade")
            shopMenu(upgrade1, upgrade2, upgrade3, gold)
        else:
            return 2
    if choice == 4:
        return 3


def miniGame():
    for mode in range(1, 4):
        if mode == 1:
            modeName = "Easy"
        if mode == 2:
            modeName = "Normal"
        if mode == 3:
            modeName = "Impossible"
        print(mode, ".", modeName)
    difficulty = (input("chose the difficulty"))
    # checks to make sure number entered is valid
    try:
        difficulty = int(difficulty)
    except:
        print("Invalid selection. Try again.")
        miniGame()
    if difficulty > 3:
        difficulty = int(difficulty)
        print("Invalid selection. Try again.", sep="")
        miniGame()
    if difficulty < 1:
        difficulty = int(difficulty)
        print("Invalid selection. Try again.", end="")
        miniGame()
    if difficulty == 1:
        wrongloop = 0
        while wrongloop == 0:
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
                    wrongloop = 1
                    if (guess % 2) == 0:
                        print("you chose an even number")
                    if guess == 1 or guess == 2:
                        print("You win!")

            except:
                print("Invalid selection. Try again.")
    if difficulty == 2:
        wrongloop = 0
        while wrongloop == 0:
            guess = input("try to guess the same number as the computer. The"
                          " computer will guess 1 or 2")
            computerguess = random.randrange(1, 3)
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
                    wrongloop = 1
                    if guess != (not computerguess):
                        print("You win!")
                    else:
                        print("You Lost!")
                        print("the computer chose", computerguess)


            except:
                print("Invalid selection. Try again.")
    if difficulty == 3:
        wrongloop = 0
        while wrongloop == 0:
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
                    wrongloop = 1
                    if guess == 1 and guess == 2:
                        print("You win!")
                    else:
                        print("You Lost!")
                        print("the computer chose 11")

            except:
                print("Invalid selection. Try again.")


# looping the menus
shopLoop = 0
while shopLoop == 0:
    destination = locationMenu()
    if destination == 0:
        shopLoop = 1
        level += 1
    if destination == 1:
        upgrade = shopMenu(upgrade1, upgrade2, upgrade3, gold)
        if upgrade == 0:
            cost = int((200 ** math.log2(upgrade1 * 1.1)) // 1)
            gold -= cost
            upgrade1 += 1
            baseDamage += 1
            print("Your Base Damage is now", baseDamage)
        elif upgrade == 1:
            cost2 = 75 * (upgrade2 ** 1.002) // 1
            gold -= cost
            upgrade2 += 1
            playerHP = playerHP * 2
            print("Your hit points is now", playerHP)
        elif upgrade == 2:
            cost3 = 1000 * (upgrade3 ** 1.001) // 1
            gold -= cost
            upgrade3 += 1
            damageMulti += 0.02
            print("Your Damage Multiplier is now", damageMulti)
        elif upgrade == 3:
            # I forget how to make a blank if statement
            placeholder = 0
    if destination == 2:
        miniGame()

# the main loop starts here
mainLoop = 0
while mainLoop == 0:
    success = (playerHP, enemyHP, level, damageMulti, baseDamage)
    gold = afterBattle(success, gold, level)
    shopLoop = 0
    while shopLoop == 0:
        destination = locationMenu()
        if destination == 0:
            shopLoop = 1
            level += 1
        if destination == 1:
            upgrade = shopMenu(upgrade1, upgrade2, upgrade3, gold)
            if upgrade == 0:
                cost = int((200 ** math.log2(upgrade1 * 1.1)) // 1)
                gold -= cost
                upgrade1 += 1
                baseDamage += 1
                print("Your Base Damage is now", baseDamage)
            elif upgrade == 1:
                cost = 75 * upgrade2
                gold -= cost
                upgrade2 += 1
                playerHP = playerHP * 2
                print("Your hit points is now", playerHP)
            elif upgrade == 2:
                cost = 1000 * upgrade3
                gold -= cost
                upgrade3 += 1
                damageMulti += 0.02
                print("Your Damage Multiplier is now", damageMulti)
            elif upgrade == 3:
                # I forget how to make a blank if statement
                placeholder = 0
        if destination == 2:
            miniGame()
