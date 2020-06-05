#!/usr/bin/env python
# coding: utf-8

# In[33]:


def display(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# In[34]:


board = ['O',' ',' ',' ',' ',' ',' ',' ',' ',' ']


# In[35]:


display(board)


# In[36]:


def check(board):
    if (board[1] == board[2] == board[3]) and board[1] !=' ':
        return True
    if (board[4] == board[5] == board[6]) and board[4] !=' ':
        return True
    if (board[7] == board[8] == board[9]) and board[7] !=' ':
        return True
    if (board[1] == board[5] == board[9]) and board[1] !=' ':
        return True
    if (board[2] == board[4] == board[8]) and board[2] !=' ':
        return True
    if (board[3] == board[5] == board[7]) and board[3] !=' ':
        return True
    
    return False


# In[37]:


def game():
    start = input("Ready to start the game ( Y or N ) : ")
    if start == 'Y':
        P1 = 'Z'
        while P1!='X' and P1!='O':
            P1 = input("Player 1, choose your symbol (X or O) : ")
            if P1!='X' and P1!='O':
                print("PLease choose the symbol from the options given....")
        if P1 == 'X':
            P2 = 'O'
        else:
            P2 = 'X'
        i = 0
        while(i<9):
            index = 'Z'
            display(board)
            while index.isdigit() == False:
                index = input("Player 1 where do you want to insert you symbol ( 1 - 9) : ")
                if index.isdigit() == False:
                    print("Please enter a digit in between 1 to 9")
                if index.isdigit() == True and board[int(index)]!=' ':
                    print("Choose another index please, this one is already occupied..")
                    index = 'Z'
                    
            board[int(index)] = P1
            i = i+1
            display(board)
            if check(board) == True:
                print("Player 1 won the game....")
                return "1"
                break
            if i == 9:
                break
                
            index = 'Z'
            while index.isdigit() == False:
                index = input("Player 2 where do you want to insert you symbol ( 1 - 9) : ")
                if index.isdigit() == False:
                    print("Please enter a digit in between 1 to 9")
                if index.isdigit() == True and board[int(index)]!=' ':
                    print("Choose another index please, this one is already occupied..")
                    index = 'Z'
                    
            board[int(index)] = P2
            i = i+1
            display(board)
            if check(board) == True:
                print("Player 2 won the game....")
                return "2"
                break
        if check(board) == False:
            print("Match is Draw..")
    else:
        print("your loss!!")
            
            


# In[ ]:


game()


# In[ ]:




