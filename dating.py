#!/usr/bin/env python3
#
# Created by: Hertz Antonella
# Created on: Apr 5 2022
# This program ask the host to answer questions using
# yes/no 


def main():
    # Ask the  user if they are rich and good looking
    ask_user1 = input("are you rich (yes/no): ")
    ask_user2 = input("are you good (yes/no): ")
    print("")

    # compare the number entered to random_variable
    if ask_user1 == "yes" or ask_user2 == "yes":
        print("you can date my grandchild!")
    elif ask_user1 == "no" and ask_user2 == "no":
        print("you can not date my grandchild")
    else:
        print("please enter valid answer")
        print("Thanks for coming")


if __name__ == "__main__":
    main()
