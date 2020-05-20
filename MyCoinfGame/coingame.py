from random import randint
from six.moves import input
x = 1
while(x==1):
    guessSide = input("\n\n****This is a coin flip game**** \n *****ENJOY***** \n\n Enter your choice: ")

    if guessSide == "HEAD" or guessSide == "head" or guessSide == "Head":
        guessNum = 1
    elif guessSide == "TAIL" or guessSide == "tail" or guessSide == "Tail":
        guessNum = 2    
    else:
        print("Invalid choice: please enter head or tail \n Exiting Game....")
        exit()

    randSide = randint(1,2)

    if randSide == 1:
        realSide = "HEAD"
    else:
        realSide = "TAIL"    
    
    if guessNum == randSide:
        print("\n********** CONGRATULATIONS **********\n***** YOU WIN *****\n")
        x = int(input(" 1.Play again\n 2.Quit\n Enter your choice: "))
    else:
        print("\n IT IS %s\n\n YOU HAVE LOST\n\n" % realSide)
        x = int(input(" ***** \n 1.Try again\n 2.Quit\n Enter your choice: "))
    if x!=1 and x!=2:
        print("Invalid choice\nExiting game...\n")
        exit()


