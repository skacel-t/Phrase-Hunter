class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guessed_letters):
        printed_phrase = []
        for letter in self.phrase:            
            if letter in guessed_letters or letter == " ":
                printed_phrase.append(letter)
            else:
                printed_phrase.append("_")
        printed_phrase = " ".join(printed_phrase)
        print(f"\n{printed_phrase}\n")

    def check_letter(self, guessed_letter):
        return guessed_letter in self.phrase

    def check_complete(self, guessed_letters):
        # phrase is more than one word, so must contain a space
        return set(self.phrase).issubset(set(guessed_letters).union(set(" ")))
