from phrasehunter import game

if __name__ == "__main__":
    game_instance = game.Game()
    game_instance.start()
    playing = True
    while playing:
        try:
            play_again = input("Would you like to play again? [yes/no]  ")
            if play_again.lower() not in ("yes", "no"):
                raise Exception("\nPlease enter 'yes' or 'no'.\n")
        except Exception as er:
            print(er)
        else:
            if play_again.lower() == "no":
                playing = False
                print("\nThanks for playing, goodbye!")
            elif play_again.lower() == "yes":
                game_instance = game.Game()
                game_instance.start()


