import random
from phrasehunter import phrase


class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [phrase.Phrase("Break a leg"), phrase.Phrase("A perfect storm"),
                        phrase.Phrase("Raining cats and dogs"), phrase.Phrase("When pigs fly"),
                        phrase.Phrase("No pain no gain")]
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        welcome_message = "Welcome to the Phrase Hunters game!"
        message_border = "-" * len(welcome_message)
        print(f"\n{message_border}\n{welcome_message}\n{message_border}")

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        self.active_phrase.display(self.guesses)

        running = True
        while running:
            try:
                user_guess = self.get_guess()
                if user_guess.lower() not in list("abcdefghijklmnopqrstuvwxyz"):
                    raise Exception("\nInvalid input. Please enter one letter.\n")
                if user_guess in self.guesses:
                    raise Exception("\nYou already guessed this letter.\n")
            except Exception as er:
                print(er)
            else:
                self.guesses.append(user_guess)
                if user_guess not in self.active_phrase.phrase:
                    self.missed += 1
                    # tackling singular vs plural
                    if 5 - self.missed == 1:
                        vite = "life"
                    else:
                        vite = "lives"
                    print(f"\nThat's a miss, you have {5 - self.missed} {vite} remaining!")

                self.active_phrase.display(self.guesses)

                # check below if phrase is not guessed and have less than 5 misses
                running = not self.active_phrase.check_complete(self.guesses) and self.missed < 5

        # if we missed 5 times, print lost statement, otherwise print won statement
        self.game_over(self.missed >= 5)

    def get_random_phrase(self):
        # could also use shuffle and pop() if I don't want repeats
        return random.choice(self.phrases)

    # if letter has already been guessed, bring up exception
    def get_guess(self):
        user_guess = input("Guess a letter:  ")
        user_guess = user_guess.lower()
        return user_guess

    def game_over(self, no_lives):
        lost_message = "You ran out of lives...\n"
        won_message = "You guessed the phrase, congratulations!\n"
        if no_lives:
            print(lost_message)
        else:
            print(won_message)
