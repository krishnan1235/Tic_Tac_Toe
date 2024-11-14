def setupboard():
    l=[]
    k=['+--- ','---',' ---+']
    l.append(k)
    for i in range(3):
        k=['| ',' ',' | ',' ',' | ', ' ',' | ']
        l.append(k)
        p=['+--- ','---', ' ---+']
        l.append(p)
    return l    
def display(l):
    for i in l:
        print(*i,sep='')
def setupcol(c):
    if c==2:
        c+=1
    elif c==3:
        c+=2
    return c   
def setuprow(r):
    if r==2:
        r+=1
    elif r==3:
        r+=2
    return r 
def winner(board):
    if board[0][0]==board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][0]==board[0][1]==board[0][2]:
        return board[0][0]   
    elif board[0][0]==board[1][1]==board[2][2]:
        return board[0][0]  
    elif board[2][0]==board[2][1]==board[2][2]:
        return board[2][0]  
    elif board[0][2]==board[1][2]==board[2][2]:
        return board[0][2]
    elif board[0][2]==board[1][1]==board[2][0]:
        return board[0][2]      
    elif board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]   
    elif board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]   
    else:
        return 'F'
def Game():
    count=9
    print()
    player1=0
    player2=0
    temp=[['0' for i in range(3)]for i in range(3)]
    while(1):
        print('Player1 Enter Your Coin Type:')
        print( 'X - 1')
        print('O - 2')
        print("_____________")
        c1=input()  
        print()
        if c1!='1' and c1!='2':
            print('Enter a Valid Input')
        else:
            break
    # while(1):    
    #     print()
    #     print('Player2 Enter Your Coin Type:')
    #     print('X - 1')
    #     print('O - 2')
    #     print("_____________")
    #     c2=input()
    #     if c2==c1:
    #         print('This type of coin was already taken')
    #     elif c2!='1' and c2!='2':
    #         print('Enter a Valid Input')
    #     else:
    #         break
    #     print()
    if c1=='1':
        c1='X'
        c2='O'
    else:
        c1='O'
        c2='X'
    while (player1!=1 and player2!=1 and count!=0):
        print()
        while(1):
            row1,col1=map(int,input('Player1 Enter row and colum for your coin:').split())
            if col1<1 or row1<1 or col1>3 or row1>3:
                print('Enter a Valid input')
                continue
            trow1=setuprow(row1)
            tcol1=setupcol(col1) 
            if board[trow1][tcol1]!=' ':
                print('This Place Were Already Taken')
            else:
                break
        board[trow1][tcol1]=c1 
        temp[row1-1][col1-1]=c1
        count-=1
        if count==0:
            break
            
        display(board)
        c=winner(temp)
        if c==c1:
            player1=1
            break
        while(1):  
            row2,col2=map(int,input('Player2 Enter row and colum for your coin:').split())
            if col2<1 or row2<1 or col2>3 or row2>3:
                print('Enter a Valid input')
                continue
            print()
            trow2=setuprow(row2)
            tcol2=setupcol(col2)
            if board[trow2][tcol2]!=' ':
                print('This Place Were Already Taken')
            else:
                break
        print('\n')    
        board[trow2][tcol2]=c2
        temp[row2-1][col2-1]=c2
        display(board)
        count-=1
        c=winner(temp)
        if c==c2:
            player2=1
            break
        # if c=='F':
        #     continue
        # elif c=='X' and c1=='X':
        #     player1=1
        # elif c=='X' and c2=='X':
        #     player2=1
        # elif c=='O' and c1=='O':
        #     player1=1
        # elif c=='O' and c2=='O':
        #     player2=1
    if count==0:
        return 3
    if player1==1:
        return 1
    return 2    
true=1
while(true):
    print('-------------------TIC TAC TOE--------------------')
    print('New Game - 1')
    print('Exit - 2')
    print('__________________________________________________')
    val=int(input())
    if val==1:
        board=setupboard()
        display(board)
        win=Game()
        if win==3:
            print('The Match is Draw')
        else:    
            print(f'The Winner is Player{win}')
    elif val==2:
        true=0
    else:
        print()
        print('Please enter a valid input')


  
 
    