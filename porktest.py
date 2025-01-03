'''
Test module created to test various aspect of PORK
Running this script should prompt user for desired tests
The user can enter the file or events they want to test
Perhaps testing can be automated as more features are added
And maybe testing could even be seperate from development
Initial code by coderchameleon
'''

# Importing any modules we would like to test
import porkcombat

def bearEncounterGameTest():
    print("TESTING Bear Encounter. Thanks for for testing this!")
    # Encounter is set up in an attempt to simulate production environment (how the player might experience it)
    porkcombat.bearEncounterInitializer()
    print("TESTING Complete")
    continueTesting = input("Would you like to keep testing (y/n)?")
    return continueTesting

def main():
    print("Welcome to porktest.py!")
    # Testing starts

    continueTesting = "y"
    currentTests = {1: bearEncounterGameTest}
    while continueTesting == "y":
        # Print out current Tests
        print("Here is a list of current tests:")
        for test in currentTests:
            print(str(test) + " - " + str(currentTests[1]))
        # Tests in the dictionary are integer indexed. Using try/except to handle input issues
        try:
            selectedTest = int(input("Which test would you like to run (test number or enter 0 to quit)? "))
            if selectedTest == 0:
                break
            # Running the tests.. test function returns value for continueTesting
            # Function to ask this, called here, would probably be better, not sure
            if selectedTest in currentTests:
                print("\nInitiating " + str(currentTests[selectedTest]))
                runSelectedTest = currentTests.get(selectedTest)
                continueTesting = runSelectedTest()
            else:
                print("Please enter a number corresponding to one of the tests.")
        except:
            print("Something wrong. Let's try that again.")
    print("Testing Ended")

# This doesn't work like I expected. Currently, in order to run tests scripts, pork.gametitle() must be commented out
if __name__ == "__main__":
    main()


