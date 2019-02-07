from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
        """
            +-------+
            |
            |
            |
            |
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |
            |
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |         |
            |
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |        -|
            |
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |        -|-
            |
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |        -|-
            |        /
            |
        ============
        """,
        """
            +-------+
            |         |
            |         0
            |        -|-
            |        / \
            |
        ============
        """]
    print(graphic[hangman])

def start():
    print("Let's play a game of Linux Hangman")
    while game():
        pass
    scores()

def game():
    dictionary = ['gnu','kernel','linux','magiea','penguin','ubuntu']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You have already picked {}".format(letter))
            else:
                letters_tried += letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry {} isn't what you are lookiing for.".format(letter))
                else:
                    print("Congratulations {} is correct.".format(letter))
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another.")

        hangedman(letters_wrong)
        print(" ".join(clue))
        print("Guesses: ", letters_tried)

        if letters_wrong ==tries:
            print("Game Over")
            print("The Word was '" + word + "'.")
            computer_score += 1
            break
        if "".join(clue) == word:
            print("You win!")
            print("The Word was '" + word + "'.")
            player_score += 1
            break
    return play_again()

def guess_letter():
    print("")
    letter = input("Make a guess for the word: ")
    letter.strip()
    letter.lower()
    print("")
    return letter

def play_again():
    answer = input("Would you like to play again: ")
    answer.lower()
    if answer in ("y","yes","of course"):
        return answer
    else:
        print("\nThank you very much for playing the game.")

def scores():
    global player_score,computer_score
    print("\nHIGH SCORES")
    print("Player: ",player_score)
    print("Computer: ",computer_score)

if __name__ == "__main__":
    start()
