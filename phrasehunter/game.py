import random
from phrasehunter import phrase


class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = ["Break a leg", "A perfect storm", "Raining cats and dogs", "When pigs fly", "No pain no gain"]
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        welcome_message = "Welcome to the Phrase Hunters game!"
        message_border = "-" * len(welcome_message)
        print(f"\n{message_border}\n{welcome_message}\n{message_border}")

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        my_phrase = phrase.Phrase(self.active_phrase)
        my_phrase.display(self.guesses)

        running = True
        while running:
            # EXCEPTIONS NEED WORK, TACKLE ALREADY USED LETTERS!!!
            try:
                user_guess = self.get_guess()
                if user_guess not in list("abcdefghijklmnopqrstuvwxyz"):
                    raise Exception("\nPlease only enter one lowercase letter.\n")
                if user_guess in self.guesses:
                    raise Exception("\nYou already guessed this letter.\n")
            except Exception as er:
                print(er)
            else:
                self.guesses.append(user_guess)
                if user_guess not in my_phrase.phrase:
                    self.missed += 1
                    # tackling singular vs plural
                    if 5 - self.missed == 1:
                        vite = "life"
                    else:
                        vite = "lives"
                    print(f"\nThat's a miss, you have {5 - self.missed} {vite} remaining!")

                my_phrase.display(self.guesses)

                # check below if phrase is not guessed and have less than 5 misses
                running = not my_phrase.check_complete(self.guesses) and self.missed < 5

        # if we missed 5 times, print lost statement, otherwise print won statement
        self.game_over(self.missed >= 5)

    def get_random_phrase(self):
        # could also use shuffle and pop() if I don't want repeats
        return random.choice(self.phrases)

    # if letter has already been guessed, bring up exception
    def get_guess(self):
        user_guess = input("Guess a letter:  ")
        return user_guess

    def game_over(self, no_lives):
        lost_message = "You ran out of lives... Thanks for playing!\n"
        won_message = "You won! Thanks for playing!\n"
        if no_lives:
            print(lost_message)
        else:
            print(won_message)
