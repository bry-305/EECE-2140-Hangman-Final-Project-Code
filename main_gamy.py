#ATTEMPT 1 - 7 remaining
# ____
# |/   |
# |
# |
# |
# |
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |
# |
# |
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |    |
# |    |
# |
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |   \|
# |    |
# |
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |   /
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |   / \
# |
# |_____
# """;
# """
#  ____
# |/   |
# |   (_)
# |   /|\
# |    |
# |   | |
# |
# |_____


def get_word():
   word = input("Input the word that you want your friend to guess (has to be 5 letters)")

   if len(word) != 5:
      print("The length of the word has to be 5 letters. Try another one.")
       #add code here so the student can input a new word if the length isn't 5 letters
   return word.upper()


#maybe add a hint option?


def get_guess():
   guess = input("What is your guess?: ")
   if len(guess) == 1:

      print(f"You're guess of {guess.upper()}")
            #this is an option for if the user inputs a single letter
   return guess



def word_checker(guess):

tries = 7




# print("Hello, welcome to Hangmamn!")
#
# get_word()
#
# while tries > 5:
#    play_game()



print("Hello, welcome to Hangmamn!")

word = get_word()

print(word)



