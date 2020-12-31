from random import *
import new.hangman.grapics as gp
import my_module


def start():
    my_module.text_image(my_module.start)
    print('+-------------------------+')
    print('| WELCOME TO HANGMAN GAME |')
    print('+-------------------------+')
    global player_scores, computer_scores
    player_scores =0
    computer_scores = 0
    while game():
        pass
    scores()


def game():
    dictionary = ['windows', 'linux', 'ubuntu', 'kali', 'parrot', 'android']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6
    letter_tries = ''
    letter_wrong = 0
    global player_scores, computer_scores


    while (letter_wrong != tries) and (''.join(clue) != word):
        print('===================')
        print('clue =',word_length)
        print('===================')
        print('\n')
        letter = guess()
        print('\n')
        if len(letter) == 1 and letter.isalpha():
            if letter_tries.find(letter) != -1:
                print('your are already choice', letter)

            else:
                letter_tries += letter + ' '
                index = word.find(letter)
                if index == -1:
                    letter_wrong += 1
                    print('you pick the wrong letter ',letter)

                else:
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
                            print('you pick the correct letter ', letter)



        else:
            print('another letter')

        gp.hangman(letter_wrong)
        print('word:',''.join(clue))
        print('guesses: ',letter_tries)

        if letter_wrong == tries:
            my_module.text_image(my_module.you_lost)
            print('game over')
            print('you lose, the word is ',word)
            computer_scores += 1
            break


        elif (''.join(clue)) == word:
            my_module.text_image(my_module.you_win)
            print('you win !')
            print('the word is ',word)
            player_scores += 1
            break


    return play_again()

def guess():
    answer = input('enter the letter: ')
    answer.strip()
    answer.lower()
    return answer

def play_again():
    answer = input('do you want to play again ?')
    if answer in ('y','Y','yes','Yes','YES'):
        return game()

    else:
        print('Thank You for playing our game !!!')


def scores():
    global player_scores, computer_scores
    my_module.text_image(my_module.game_over)
    print("HIGH SCORE")
    print('player = ',player_scores)
    print('computer = ',computer_scores)

if __name__ == '__main__':
 start()



