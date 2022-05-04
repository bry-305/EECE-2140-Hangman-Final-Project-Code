import random
from words import word_list
from hangman_pictures import print_picture



class GetInfo:

    def __init__(self):

        self.choice = int(input("How many people are playing? '1' or '2' people?: "))
        if self.choice == 2:
            self.word = input("What word do you want to play?: ").upper()
            self.hint = input("Would you like to give a hint? If not just press 'enter': ")
        else:
            self.word = random.choice(word_list).upper()
            self.hint = "There is no hint because you're playing single player :( "

    def Hint(self):
            return self.hint

    def Word(self):
            return self.word


    def displayWord(self):
        print(self.word)
        return self.word


class PlayGame:

    def __init__(self):
      pass


    def Hangman(self, word, hint):


        play_again = True
        while play_again == True:
            tries = 7
            correct = []
            wrong = []
            game_status = True
            word = word
            blank_word = "_" * len(word)



            print(20 * "\n")

            print("Type 'Hint' if you'd like to use a hint")
            print("\n")

            print(blank_word)

            while (tries > 0) & (game_status == True) & (play_again == True):
                guess = input("Letter to input?: ").upper()
                print("\n" * 2)

                if guess == "HINT":
                    print(f"You're hint is '{hint}'")

                elif guess not in (correct or wrong):
                    if guess in word:
                        print(f"Yes '{guess}' is in the word!")
                        print(f"You have {tries} tries left!")
                        correct.append(guess)
                        for i in range(len(word)):
                            if word[i] in correct:
                                blank_word = blank_word[:i] + word[i] + blank_word[i + 1:]
                        print(blank_word, end=" ")
                        print(f"Used letters [{correct}, {wrong}]")
                        print_picture(tries)


                    else:
                        print(f"No, '{guess}' is not in the word :) ")
                        wrong.append(guess)
                        tries -= 1
                        print(f"You have {tries} tries left!")
                        print("\n")
                        print(blank_word, end=" ")
                        print(f"Used letters [{correct}, {wrong}]")
                        print_picture(tries)

                else:
                    print(f"You already guessed {guess}, try another! ")

                if tries == 0:
                    print("Sorry you are out of tries")
                    print(f"The correct word was '{word}'")
                    resume = input("Would you like to keep playing? (Yes or No): ").upper()
                    if resume == "YES":
                        play_again = True
                    else:
                        play_again = False

                    game_status = False

                if blank_word == word:
                    print("You won the game!")
                    print("\n" * 3)
                    resume = input("Would you like to keep playing (Yes or No): ").upper()
                    if resume == "YES":
                        play_again = True
                    else:
                        play_again = False

                    game_status = False

        print("\n")
        print("Thank You for playing!!")









game = GetInfo()

hint = game.Hint()
word = game.Word()

game = PlayGame()
game.Hangman(word, hint)