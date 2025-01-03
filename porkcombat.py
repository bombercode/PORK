'''
Combat module created for the porklogic.py file
Functions handling combat are organized here
If more enemies are added, A seperate file
To aid with enemy creation could be added 
Initial code by coderchameleon
'''

# we need to get Hammy's health
import pork

# Called when it is time for Hammy to fight a bear
def bearEncounterInitializer():
    # First, we initialize our bear with some simple moves and their damage
    # We also include some moves for Hammy to test
    bearHealth = 3
    bearAbilities = {"Roar": 0 , "Maul": 1, "Bite": 1}
    hammyAbilities = {"Roar": 0, "Punch": 1}
    # The best case encounter for Hammy affects the fight
    # TODO Probably ADD Global Bool to replace test flag
    print("CREATING A TEST FLAG")
    print("USED FOR TESTING ONLY")
    bestCaseScenario = True
    print("OUR BEST CASE SCENARIO FLAG IS SET TO " + bestCaseScenario)
    # Fight encounter loop
    # Currently just cylces through bear abilities
    for ability in bearAbilities:
        # If Hammy is alive or it's the best case scenario, the fight continues
        while(hammyIsAlive() or bestCaseScenario):
            # Bear uses its ability (printed in the console) and lowers Hammy's health if applicable
            print("Bear uses " + ability)
            pork.health -= bearAbilities[ability]
            # If Hammy can die and has died, the function (fight) ends, False is returned in this situation
            if not bestCaseScenario and not hammyIsAlive():
                print("You have become bacon")
                return False
            # Calls a function to handle the move selected by the player
            hammySelectedAbility = selectHammyAbility(hammyAbilities)
            bearHealth -= hammyAbilities[hammySelectedAbility]
            #if the bear has been defeated, the function (fight) ends, True is returned in this situation
            if bearHealth <= 0:
                print("The bear has been defeated!")
                return True
        # If all goes well, the following shouldn't occur
        print("exception met: ")
        print("Hammy must be bacon")
        return False

            
def selectHammyAbility(hammyAbilities):
    # Getting ability selection and using tolower function to normalize input
    print("What do you do?")
    for ability in hammyAbilities:
        print(ability)
    hammySelectedAbility = input().lower()
    # If invalid input is given, the while loop is executed to get new input
    while(hammySelectedAbility not in hammyAbilities):
        print("Please enter one of the following abilities: ")
        for ability in hammyAbilities:
            print(ability)
        hammySelectedAbility = input().lower()
    # Return the selected ability
    return hammySelectedAbility
    


def hammyIsAlive():
    # Checks to see if Hammy has any life points left
    if pork.health > 0:
        return True
    else:
        return False
        