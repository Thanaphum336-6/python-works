import os
import random
import time
import sqlite3
conn = sqlite3.connect(r"C:/Users/Admin/Desktop/Project OS/Database/Databasetest1.db")
c = conn.cursor()

def deletedata():
    try :
        c.execute("DELETE from lose")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'lose' ")
        c.execute("DELETE from Win")
        c.execute("DELETE FROM sqlite_sequence WHERE name = 'win' ")
        c.execute('''insert into Win (win,counts) VAlUES(0,1)''')
        c.execute('''insert into lose (lose,counts) VAlUES(0,1)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)
    finally :
        if conn :
            conn.close()
    print('success')
    time.sleep(1)        
    option() 

def welcome():
    for i in range(0, 11):
        print("x", end="")
    print()
    print("* WELCOME *", end="")
    print()
    for i in range(0, 11):
        print("x", end="")
    print()
    input("Press ENTER key to start")

def option():
    for i in range(0, 21):
        print("X", end="")
    print()
    print("1)Player vs Player\n2)Vs bot\n3)ResetWinrate")
    for i in range(0, 21):
        print("X", end="")
    print()
    Playerinput = int(input("Enter your choice number: "))
    if Playerinput == 1:
        two_player()
    elif Playerinput == 2:
        Play_with_Bot()
    elif Playerinput == 3:
        deletedata()
        
    else:
        welcome()

def two_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to Player Vs Player")
        print("This is a two player game where Player 1 is X and Player2 is O")
        print("Enter your pos from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    while True:
        os.system("cls")
        rules()
        print_board()

        # user 1
        choice = input("Player1 Turn (X): ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("pos already taken")
            time.sleep(1)
        # player 1 win
        if is_winner(board, "X"):
            os.system("cls")
            rules()
            print_board()
            print("Player1 Win")
            break

        os.system("cls")
        rules()
        print_board()

        # เช็คเสมอ
        if is_board_full(board):
            print("Tie")
            break

        # player 2

        choice = input("Player2 Turn (O): ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Spot already taken")
            time.sleep(1)
        # player 2 win
        if is_winner(board, "O"):
            os.system("cls")
            rules()
            print_board()
            print("Player2 Win")
            break

        # เช็คเสมอ
        if is_board_full(board):
            print("Tie")
            break

def Play_with_Bot():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Welcome to XXX OOO")
        print("Player = X  Bot = O")
        print("Enter your pos from 1 to 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9""")
                

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def win_con(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    def bot_move(board, player):

        # bot ลง ดัก
        for i in range(1, 9):
            if board[i] == " ":
                board[i] = player
                if win_con(board, player):
                    return i
                else:
                    board[i] = " "

        # bot เช็ค ลงแนวตั้ง
        for i in [1, 2, 3]:
            if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                return i+6
            if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                return i+3

        # bot เช็ค ลงแนวนอน
        for i in [1, 4, 7]:
            if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                return i+2
            if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                return i+1

        # bot เช็ค ลงแนวแทยง
        if board[1] == "X" and board[5] == "X" and board[9] == " ":
            return 9
        if board[9] == "X" and board[5] == "X" and board[1] == " ":
            return 1
        if board[1] == "X" and board[9] == "X" and board[5] == " ":
            return 5
        if board[3] == "X" and board[5] == "X" and board[7] == " ":
            return 7
        if board[7] == "X" and board[5] == "X" and board[3] == " ":
            return 3
        if board[3] == "X" and board[7] == "X" and board[5] == " ":
            return 5

        if board[5] == " ":
            return 5

        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                return move
                break
            return 5

    while True:
       
        os.system("cls")
        rules()
        print_board()

        # player
            
        choice = input("Please choose an empty space for X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X" 

        else:
            print("Spot already taken")
            time.sleep(1)
        
            

        # player check ชนะ
        if win_con(board, "X"):
            os.system("cls")
            rules()
            print_board()
            print("Haha!!You Win")
            c.execute('''insert into Win (win,counts) VAlUES(Null,1)''')
            c.execute('''SELECT MAX(lose) FROM lose''')
            result = c.fetchone()
            for x in result :
                print('Loses:',x)
            c.execute('''SELECT MAX(Win) FROM win''')
            result = c.fetchone()
            for e in result :
                print('Wins:',e)
            winrate = e/(e + x)*100
            print('Your Winrate is:',winrate,'%')
            conn.commit()
            c.close()
            
        

        os.system("cls")
        rules()
        print_board()

        # player check เสมอ
        if is_board_full(board):
            print("Tie")
            c.execute('''SELECT MAX(lose) FROM lose''')
            result = c.fetchone()
            for x in result :
                print('Loses:',x)
            c.execute('''SELECT MAX(Win) FROM win''')
            result = c.fetchone()
            for e in result :
                print('Wins:',e)
            winrate = e/(e + x)*100
            print('Your Winrate is:',winrate,'%')
            break

        # Bot
        choice = bot_move(board, "O")
        if board[choice] == " ":
            board[choice] = "O"
       
        # Bot check ชนะ
        if win_con(board, "O"):
            os.system("cls")
            rules()
            print_board()
            c.execute('''insert into lose (lose,counts) VAlUES(Null,1)''')
            print("Haha!! You lose the fking bot")
            c.execute('''SELECT MAX(lose) FROM lose''')
            result = c.fetchone()
            for x in result :
                print('Loses:',x)
            c.execute('''SELECT MAX(Win) FROM win''')
            result = c.fetchone()
            for e in result :
                print('Wins:',e)
            winrate = e/(e + x)*100
            print('Your Winrate is:',winrate,'%') 
            conn.commit()
            conn.close()
            
            break

        # bot check เสมอ
        if is_board_full(board):
            print("Tie")
            c.execute('''SELECT MAX(lose) FROM lose''')
            result = c.fetchone()
            for x in result :
                print('Loses:',x)
            c.execute('''SELECT MAX(Win) FROM win''')
            result = c.fetchone()
            for e in result :
                print('Wins:',e)
            winrate = e/(e + x)*100
            print('Your Winrate is:',winrate,'%')
            break

welcome()
option()

