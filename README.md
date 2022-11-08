# Rock, Paper, Scissors, Lizard, Spock game
Rock, Paper, Scissors, Lizard, Spock game was created using python and will run in the command line. It allows the user to test their luck against the computer to get the highest possible score.

## Features
This command-line based Python game allows you pick the number of games you want to play against the computer and get the highest score you can.
The computer will be picking randomly between Rock, Paper, Scissors, Lizard and Spock, for every game the player wins they gain 100 points and for every game they tie the player gets 50 points, and 0 points for losing a game.

* When the program is started the player will be greeted with introduction to the game and will be asked for their name for the high score.

![intro-game](https://user-images.githubusercontent.com/20689249/200134390-9eccefa9-2f82-4b62-bf44-37e8c2fc27bd.png)

* Once the player has entered their name, they are then asked how many games they would like to play against the computer (in this example 10 games have been chosen)
the program will continue to run till the number of games chosen have been played out.

![first game](https://user-images.githubusercontent.com/20689249/200134595-d170e79d-c75e-4552-86a9-57d6726de403.png)

* When an invalid option is chosen the player will be shown an error message and to try again

* Once all the games are finished the player will be shown their score and a little message of encouragement

![game1](https://user-images.githubusercontent.com/20689249/200134890-9e5da040-18aa-4ccb-ac12-5799edead55c.png)

* If the player does happen to input 0 for the number games to play the game will end and will need to be started again

![0games](https://user-images.githubusercontent.com/20689249/200135958-509957ce-1edd-49a4-a296-78e34ba5d7a5.png)

## Features Left to Implement
* A high scores list that features the top 10 scores and the player's name
* Have the option to allow players input a single letter or number to represent their choice rather than the full word
* Have the option to allow players to input actions for multiple games at once and getting a total score at the end rather than every game.

## Testing
* Thorough testing has been conducted to ensure that the site works well. A random result for each of the player's input for each game as intended.
* The game also takes note of the player's total score and reports it back to them as intended
* The total number of games the player will play is the number they input at the start of the game as intended

### Fixed Bugs
* A continuous loop had kept occurring but, was solved after adding "break"
* While loop for the game did not work as intended at first, but was fixed after the correct indentations of the statements

## Credits
+ [W3Schools Python Random randint](https://www.w3schools.com/python/ref_random_randint.asp) was used as reference in the website
+ [W3Schools Conditions and If statements](https://www.w3schools.com/python/python_conditions.asp) was used as reference in the website
+ [W3Schools While loops](https://www.w3schools.com/python/python_while_loops.asp) was used as reference in the website
+ [W3Schools Arrays](https://www.w3schools.com/python/python_arrays.asp) was used as reference in the website
