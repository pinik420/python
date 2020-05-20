from Linkedlist import Linkedlist


linkedlist = Linkedlist()

linkedlist.insertEnd(12)
linkedlist.insertEnd(122)
linkedlist.insertEnd(3)
linkedlist.insertStart(31)

linkedlist.traverseList()
while 1:
    b=input(" 1. Add number to list end \n 2. Add number to list start \n 3. Remove number \n 4. Print list \n 5. Exit \n Enter your choice: ")

    if b == 1:
        c = input("\n Enter the number: ")
        linkedlist.insertEnd(c)
    elif b == 2:
        c = input("\n Enter the number: ")
        linkedlist.insertStart(c)
    elif b == 3:
        c = input("Enter the number you want to remove: ")
        linkedlist.remove(c)
    elif b == 4:
        linkedlist.traverseList()  
    elif b == 5:
        exit()
    else:
        print("Enter a valid choice!!")




