# Created by Jennifer Souvannasing, SEC 290 Block B, Chapter 4 exercise, 07/18/22

from time import *

def get_words(word_type):
    # This function gets a noun, verb and adjective
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input('Please enter a word that is {0} {1}: '.format(a_or_an, word_type))

def fill_in_blanks(noun, verb, adjective):
    # This function fills in the blanks of the story
    my_story = "It was a cold December morning, and I woke up to the {2} smell of \nbreakfast cooking. We were having {0}! I love {0}, especially with warm tea. I ran \ndownstairs to {1} the delicious food. This was the best breakfast ever!".format(noun, verb, adjective)
    return my_story

def display_story(my_story):
    # This function displays the completed story
    print()
    slow("...Processing...")
    print('\n')
    print('Here is the story that you created. Enjoy!')
    print()
    print('-' * 75)
    print()
    print(my_story)

def create_my_story():
    # This function captures the user input for the story
    noun = get_words('noun')
    verb = get_words('verb')
    adjective = get_words('adjective')

    whole_story = fill_in_blanks(noun, verb, adjective)
    display_story(whole_story)

def slow(text):
    # This function will add some slowness to text
    for letters in text:
        print(letters, end = "")
        sleep(0.25)

create_my_story()

    
    
