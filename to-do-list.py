
import os
from datetime import date


def welcome(name):
    print(f""" WELCOME $ {name} $ TO TO_DO_LISTS APPLICATION
        1--> UPDATE LIST
        2--> TRACK LIST
        3--> exit""")


def to_do_list_create(name):
    with open(f"{name}.txt", 'a')as f:
        f.write("")
    print("To do List_File is created Successfully")


def update(name):

    print(f"Welcome, {name} to EDIT Menu")
    choice = int(
        input("Press '1' to ADD '2' to DELETE List_File: "))
    if choice == 1:
        task = input("Enter Task to ADD: ")
        with open(f"{name}.txt", 'a') as f:
            f.write(f"{task} - {date.today()}\n")

    elif choice == 2:
        try:
            os.remove(f"{name}.txt")
            print(f"{name} list_file Deleted Successfully")
        except ValueError:
            print("Something gone Wrong!!")
    else:
        print("Invalid Choice")


def track(name):
    try:
        with open(f"{name}.txt", 'r')as f:
            result = f.read()
            if result == "":
                print("No Task Here")
            else:
                print(result)
    except FileNotFoundError:
        print(
            f"List with the UserName '{name}' NOT FOUND, please first ADD your List")


name = input("Please Enter Your Name: ")
to_do_list_create(name)
while True:
    welcome(name)
    choice = int(input("Enter Choice: "))
    if choice == 1:
        update(name)
    elif choice == 2:
        track(name)
    elif choice == 3:
        exit
    else:
        print("Invalid Choice")
