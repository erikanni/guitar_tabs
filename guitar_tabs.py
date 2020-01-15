import sys
import json
import subprocess as sp

#template
#print("-----------------")
#print("-----------------")
#print("-----------------")
#print("-----------------")
#print("-----------------")
#print("-----------------")

def choice(options):
    for i in range(len(options)):
        print(i+1, options[i])
    input_is_valid = False
    while input_is_valid == False:
        user_input = input()
        try:
            val = int(user_input)
            if val > 0 and val <= len(options):
                input_is_valid = True
            else:
                print("Sorry, the number must be between 1 and ", len(options))
        except:
            print("Sorry, you must enter a number!")

    return (val-1)

def main_menu():
    while True:
        print("would you like to see guitar tabs or chords? 1 for tabs, 2 for chords, x to exit")
        user_input = input()
        if user_input == "1":
            tabs_menu()
        elif user_input == "2":
            chords_menu()
        elif user_input == "X" or user_input == "x":
            sys.exit()
        else:
            print("Please enter '1', '2' or 'X'!")
def c_major_chord():
    print("-----------------")
    print("--------1--------")
    print("-----------------")
    print("--------2--------")
    print("--------3--------")
    print("--------x--------")
    print("press b to go back or x to exit")
        user_input = input()
    if user_input == "b" or user_input == "B":
        chords_menu()
    if user_input == "x" or user_input == "X":
        sys.exit()
    else:
        print("please enter a valid option")

def a_chord():
    print("-----------------")
    print("--------2--------")
    print("--------2--------")
    print("--------2--------")
    print("-----------------")
    print("--------x--------")
    print("press b to go back or x to exit")
        user_input = input()
    if user_input == "b" or user_input == "B":
        chords_menu()
    if user_input == "x" or user_input == "X":
        sys.exit()
    else:
        print("please enter a valid option")

def g_major_chord():
    print("--------3--------")
    print("--------2--------")
    print("-----------------")
    print("-----------------")
    print("-----------------")
    print("--------3--------")
    print("press b to go back or x to exit")
        user_input = input()
    if user_input == "b" or user_input == "B":
        chords_menu()
    if user_input == "x" or user_input == "X":
        sys.exit()
    else:
        print("please enter a valid option")

def e_chord():
    print("-----------------")
    print("-----------------")
    print("--------1--------")
    print("--------2--------")
    print("--------2--------")
    print("-----------------")
    print("press b to go back or x to exit")
        user_input = input()
    if user_input == "b" or user_input == "B":
        chords_menu()
    if user_input == "x" or user_input == "X":
        sys.exit()
    else:
        print("please enter a valid option")


def d_major_chord():
    print("--------2--------")
    print("--------3--------")
    print("--------2--------")
    print("-----------------")
    print("--------x--------")
    print("--------x--------")
    print("press b to go back or x to exit")
        user_input = input()
    if user_input == "b" or user_input == "B":
        chords_menu()
    if user_input == "x" or user_input == "X":
        sys.exit()
    else:
        print("please enter a valid option")

def chords_menu():
    print("list of chords")
    print("type the number of the chord")
    user_input = input()
    if user_input == "1":
        c_major_chord()
    elif user_input == "2":
        a_chord()
    elif user_input == "3":
        g_major_chord()
    elif user_input == "4":
        e_chord()
    elif user_input == "5":
        d_major_chord()
    elif user_input == "X" or user_input == "x":
        sys.exit()
    else:
        print("Please enter a valid number")
    
def dead_man():
    print("intro")
    print("e|--------------------------------------------------------------------2----------|")
    print("B|--------------------------------------------------------------------3----------|")
    print("G|--------------------------------------------------------------------4----------|")
    print("D|-------------------------------------------------------------------------------|")
    print("A|-0-0-2-5-2----------0-0-2-5-2-------0-0-2-5-2-------4-2------------------------|")
    print("E|---------------------------------------------------------2---------------------|")
    print("solo")
    print("e|------2---------------------2---0--------2-2------------2--------------------|")
    print("B|--3-5---5-3-0-----5s7---0-----------3---------------3-5---3-2b--2s3-3s5------|")
    print("G|--------------------------------------2--------------------------------------|")
    print("D|-----------------------------------------------------------------------------|")
    print("A|-----------------------------------------------------------------------------|")
    print("E|-----------------------------------------------------------------------------|")
    print("solo")
    print("e|-2-------------2--------------------------------------------------------------|")
    print("B|---5-3-5-3-------3-----5-3-2---5-3-1-0(ring)----------------------------------|")
    print("G|-----------4-------3----------------------------------------------------------|")
    print("D|------------------------------------------------------------------------------|")
    print("A|---------------------------------------------------0-0-2-5-2------5-4-0-2-5-2-|")
    print("E|------------------------------------------------------------------------------|")

    print("WORK IN PROGRESS")

    



def tabs_menu(input):
    print("1: dead man solo")
    print("2: stairway to heaven")
    print("3: Another one Bites the dust")
    print("type the number of the song")
        user_input = input()
    if user_input == "1":
        dead_man()
    if user_input == "2":
        stairway()
    if user_input == "3":
        another_one()






#    print("")
#    print("")
#    print("")
#    print("")
#    print("")
#    print("")