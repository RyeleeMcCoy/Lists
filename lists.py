#-------------------------------------------------------------------------------
# Name: lists
# Purpose:
#
# Author:      ryelee.mccoy
#
# Created:     08/10/2019
# Copyright:   (c) ryelee.mccoy 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
userneeds = input(str("Do you need to go to the store today? type yes or no" ))
list = ["apples", "bananas", "eggs", "milk"]
storelist = []
def developerlist():
    print("You have to pick up the following from the store today", list[1])

def userlist(userneeds, storelist):
    groc = "yes"
    function = "yes"
    while function == "yes":
        if userneeds == "yes":
            while groc == "yes":
                addlist = input(str("What do you need at the store today? Type what you need, type done when you have everything! "))
                storelist.append(addlist)
                if addlist == "done":
                    print("You got everything in", storelist)
                    groc = "no"
                    function = "no"
                else:
                    print("Still need more!")
        elif userneeds == "no":
            print("Okie dokie!")
            function == "no"
        else:
            print("Thats not an option!")







developerlist()
userlist(userneeds, storelist)