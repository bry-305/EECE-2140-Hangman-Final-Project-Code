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
   print("\n")
   word = input("Input the word that you want your friend to guess: ")

   len_word = len(word)


   return word.upper()


#maybe add a hint option?


def check_guess(word):


   blank_word = "_" * len(word)
   guessed = False
   while not guessed and tries > 0:
      guess = input("Please guess a letter or word: ").upper()

   if guess in word:
      word = list(word)
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices:
          word[index] = guess
      word_complettion = "".join(word)
      if "_" not in word:
          guessed = True



   # if len(guess) == 1:
   #
   #    print(f"You're guess of {guess.upper()}")
   #          #this is an option for if the user inputs a single letter
   # return guess



tries = 7




# print("Hello, welcome to Hangmamn!")
#
# get_word()
#
# while tries > 5:
#    play_game()



print("Hello, welcome to Hangmamn!")

word = get_word()

check_guess(word)


print(word)



