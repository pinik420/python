from BinarySearchTree import BST
from os import *
bst = BST()
# bst.insert(10)
# bst.insert(1)
# bst.insert(-2)
# bst.insert(67)



# bst.insert(5)

# print( bst.getMax() )
# print ("\n")
# print(bst.getMin())
# print ("\n")

# bst.traverseInOrder()

# bst.remove(10)
# print ("\n")
# bst.traverseInOrder()
# print ("\n")


while 1:
    b=input(" 1. Add number to binarytree \n 2. Remove number \n 3. Print binarytree \n 4. Print Max \n 5. Print Min \n 6. Exit \n Enter your choice: ")

    if b == 1:
        c = input("\n Enter the number: ")
        bst.insert(c)
    elif b == 2:
        c = input("Enter the number you want to remove: ")
        bst.remove(c)
    elif b == 3:
        bst.traverseInOrder()
        
        
    elif b == 4:
        print(bst.getMax())
    elif b == 5:
        print(bst.getMin())

    elif b == 6:
        exit()
    else:
        print("Enter a valid choice!!")
