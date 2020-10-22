import numpy
import os
import sys 
import json
import tkinter as tk
from colorama import Fore, Back, Style 

sys.path.append(".")
from User import User


file_object = open("inventory.txt", "w+")

items  = [["SPECIAL", 0.0025575], ["COVERT", 0.0063939], ["CLASSIFIED", 0.0319693], ["RESTRICTED", 0.1598465], ["MILSPEC", 0.7992328]]
elems = [i[0] for i in items]
probs = [i[1] for i in items]


def find_item():
    return numpy.random.choice(elems, p = probs)

def open_case():
    currItem = find_item()
    file_object.write(currItem + '\n')
    file_object.flush()
    os.fsync(file_object.fileno())
    print_color(str(currItem))
    print(Style.RESET_ALL) 

def print_color(item):
    if item == "MILSPEC":
            print("You opened a " + Fore.BLUE + item)
    if item == "RESTRICTED":
            print("You opened a " + Fore.BLACK + item)
    if item == "CLASSIFIED":
            print("You opened a " + Fore.BLACK + item)
    if item == "COVERT":
            print("You opened a " + Fore.RED + item)
    if item == "SPECIAL":
            print("You opened a " + Fore.YELLOW + item)


def loadjson(filename):
    with open(filename) as json_file:
        return json.load(json_file)


def check_inventory():
    milspec = []
    restricted = []
    classified = []
    covert = []
    special = []
    file_object = open("inventory.txt")
    for s in file_object:
        if s == "MILSPEC\n":
            milspec.append(s)
        if s == "RESTRICTED\n":
            restricted.append(s)    
        if s == "CLASSIFIED\n":
            classified.append(s)
        if s == "COVERT\n":
            covert.append(s)
        if s == "SPECIAL\n":
            special.append(s)
        
        if not s:
            break

    print("Number of MILSPEC: " + str(len(milspec)))
    print("Number of RESTRICTED: " + str(len(restricted)))
    print("Number of CLASSIFIED: " + str(len(classified)))
    print("Number of COVERT: " + str(len(covert)))
    print("Number of SPECIAL: " + str(len(special)))


def runprog():
    print(getUser("vladlol"))
    print(getUser("cpapi"))  
    user = User("dog")
    print(user.jsonformat()) 
    
def getUser(username):
    user = loadjson(username + ".json")
    return user


    # while True:
    #     print("1 - Open Case")
    #     print("2 - Check inventory")
    #     print("3 - Exit")

    #     # listen to 192.168.0.1
    #     choice = input("Enter option:")


    #     # once we get a "request"
    #         # roll the case
    #         # get user inventory
    #     if int(choice) == 1:
    #         # execute the command
    #         open_case()
    #         # data = open_case()
    #         # send_respone(data)
    #     elif int(choice) == 2:
    #         check_inventory()
    #     elif int(choice) == 3:
    #         break

runprog()


file_object.close()
