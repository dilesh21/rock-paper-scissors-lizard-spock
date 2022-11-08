from random import randint

n = 1
score = 0
player = " "
a = ["Rock", "Paper", "Scissors", "Lizard", "Spock",]
bot = a[randint(0,4)]

print("Welcome to this Rock, Paper, Scissors, Lizard, Spock Game!! \nYou will first set the total number of games to Play!! \nFor every game you win, you get 100 points, a tie gives you 50 points!! \nSee how high you can get!!")
uName = input("Insert your name: ")
totalGames = input("How many games would you like to play? ")

while n <= int(totalGames):
    player = input("Rock, Paper, Scissors, Lizard, Spock? ")    
    if player == bot:
        print("Both picked", player, "It's a Tie! Plus 50 points")
        n += 1
        score += 50
    elif player == "Rock":
        if bot == "Paper" or bot == "Spock":
            print("You lose!", bot, "wins over", player)
            n += 1
        else:
            print(player, "wins over", bot, "You win!! Plus 100 points")
            n += 1
        score += 100
    elif player == "Paper":
        if bot == "Scissors" or bot == "Lizard":
            print("You lose!", bot, "wins over", player)
            n += 1
        else:
            print(player, "wins over", bot, "You win!! Plus 100 points")
            n += 1
            score += 100
    elif player == "Scissors":
        if bot == "Rock" or bot == "Spock":
            print("You lose...", bot, "wins over", player)
            n += 1
        else:
            print(player, "wins over", bot, "You win!! Plus 100 points")
            n += 1
            score += 100
    elif player == "Lizard":
        if bot == "Rock" or bot == "Scissors":
            print("You lose...", bot, "wins over", player)
            n += 1
        else:
            print(player, "wins over", bot, "You win!! Plus 100 points")
            n += 1
            score += 100
    elif player == "Spock":
        if bot == "Lizard" or bot == "Paper":
            print("You lose...", bot, "wins over", player)
            n += 1
        else:
            print(player, "wins over", bot, "You win!! Plus 100 points")
            n += 1
            score += 100
    else:
        print("Check your spelling! or First letter must be uppercase!")
    

totalScore = int(totalGames)*100
if int(totalGames) == 0:
    print("0 was entered for Games to play, Try again")
elif int(totalGames) == 1:     
    print(uName, "your total score for", totalGames, "game is", score, "out of", totalScore)
else:
    print(uName, "your total score for", totalGames, "games is", score, "out of", totalScore)


while totalScore > 0:
    percent = (score / totalScore) * 100  
    if percent >= 75:
        print(uName, "you won", int(percent), "percent of your games, WELL DONE!! B)")
        break
    elif percent >= 50 and percent < 75:
        print(uName, "you won", int(percent), "percent of your games, Your almost there. :)")
        break
    elif percent < 50 and percent >= 25:
        print(uName, "you won", int(percent), "percent of your games, You might want to try again. :>")
        break    
    elif percent < 25 and percent >0:
        print(uName, "you won", int(percent), "percent of your games, Go rub a Rabbit's foot :p")
        break        
    else:
        print("You played 0 games, try again")
