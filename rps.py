from ast import Return
from msilib.schema import Error
import random

list_of_choice = ('P','R','S') #the collection of available answers

right_choices = ([2,0], #this is for the instance of scissors beats paper
                [1,2], # this is for the instance of rock beats scissors
                [0,1] ) #this is for the instance of paper beats rock

choices = {'R':'Rock','P':'Paper','S':'Scissors'}#the ansers with values that define them


valid_input = True
while valid_input:
    user_choice = str(input('\nEnter your choice \n R for rock \n P for Paper \n S for Scissors \n')).upper()
    if(list_of_choice.__contains__(user_choice)):
        computer_choice=random.choice(list_of_choice)
        print('\nPlayer(',choices[user_choice],'): CPU (',choices[computer_choice],')')
        if right_choices.__contains__([list_of_choice.index(user_choice),list_of_choice.index(computer_choice)]):
            print(choices[user_choice],'beats',choices[computer_choice],'\nYou win')
            valid_input = False
        elif user_choice == computer_choice:
            print('This is a tie \n')
        else: 
            print('\n',choices[computer_choice],'beats',choices[user_choice],'\n You lose')
            valid_input = False
    else:
        print('User input doesn\'t match given choices')

