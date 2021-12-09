# Botosauras
This programs purpose is to help with managing data and offering useful tools for players who play Dungeons and dragons online with slack. 

## Functionality 
### Character Storage
We have used a json file to store our charcter stats as well as the inventory look at file Char.json to see example
### Commands 
We have a list of commands that we are still expanding on but as of right now we have the list of 
1. !A - Testing if an attack is a critical hit returns boolean
2. !R - Rolls Dice the parameters are !R (amount of dice rolled)D(number of sides on dice ex 4,8,10,12,20) (Skill change) (Advantage Neutral Disadvantge) ex !R 1D20 +2 A
3. !M - Which simulates a attack with params of (numberOfRolls)D(SidesofDice) ex !M 1D20
4. !ARP - Adds a random character params !ARP (NameOfCharacter)
5. !AP- Adds a player and will add stats if given as args also determines if the current player is the dm params !AP (Is_DM Boolean) (NameOfCharacter)

### Authors
Bryan Sullivan, Timothy Carta, Nico Vazquez, Hephzibah Rajan, Christelle Flores