# TASK 1
class Character:
    # Constructor: Properties (State)
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    # Methods (Behaviour)

    # Print Out Character’s Primary or Secondary Catch Phrase Based on the PhraseNum Argument.
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    # Set the Character’s Level Property to the newLevel Argument 
    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.level)


# TASK 2
kung_fu_panda = Character("Kung Fu Panda", "Skadoosh", "You have been blinded by pure awesomeness!")

spiderman = Character("Spiderman", "My Spider-Sense is tingling", "Your friendly neighbourhood spiderman.")

# TASK 3
kung_fu_panda.speak(1)
kung_fu_panda.setLevel(2)
spiderman.speak(2)