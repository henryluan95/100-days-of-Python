import art
import game_data
import random
print(art.logo)

def newTarget(list):
    random_index = random.randint(0, len(list))
    target = list[random_index]
    return target

def updateList(currentTarget, list):
    for i in range(len(list)):
        if list[i]['name'] == currentTarget["name"]:
            del list[i]
            return list


def printGame(ATarget, BTarget):
    print(f'Compare A: {ATarget["name"]}, a {ATarget["description"]}, from {ATarget["country"]},{ATarget["follower_count"]}')
    print(art.vs)
    print(f'Compare B: {BTarget["name"]}, a {BTarget["description"]}, from {BTarget["country"]}, {BTarget["follower_count"]}')


def hasMoreFollowers(ATarget, BTarget, guessedTarget):
    if(guessedTarget == "A"):
        if (ATarget["follower_count"] < BTarget["follower_count"]):
            return False
        else:
            return True
    elif(guessedTarget == "B"):
        if (BTarget["follower_count"] < ATarget["follower_count"]):
            return False
        else:
            return True





def game():
    ATarget = newTarget(game_data.data)
    updatedList = updateList(ATarget, game_data.data)
    BTarget = newTarget(updatedList)
    printGame(ATarget, BTarget)

    # Initial guess
    guess = input('Who has more followers? Type "A" or "B": ')
    correctGuess = hasMoreFollowers(ATarget, BTarget, guess)
    score = 0

    # While guessing right
    while correctGuess:
        score += 1
        print(f'You guess right! Current score: {score}')
        ATarget = BTarget
        updatedList = updateList( BTarget,updatedList)
        BTarget = newTarget(updatedList)
        printGame(ATarget, BTarget)
        guess = input('Who has more followers? Type "A" or "B": ')
        correctGuess = hasMoreFollowers(ATarget, BTarget, guess)

    # If guessed wrong
    if (correctGuess == False):
        print(f"Sorry, that's wrong. Final score: {score}")


game()