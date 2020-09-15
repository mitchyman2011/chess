from stockfish import Stockfish 
import time
import chess
import keyboard
sf = Stockfish("K:\Local Disk\documents\chess\stock\stockfish-11-win\stockfish-11-win\Windows\stockfish_20011801_x64_modern.exe")
print(sf.get_board_visual())
moves=[]
n=0
k=0
white,black,fold,mov50,stalemate=0,0,0,0,0
play=True
threeinrowdraw=False

while threeinrowdraw==False:
    
    time.sleep(2)
    moves=[]
    n=0
    sf.set_position(moves)
    play=True
    board = chess.Board()
    while play==True:
         
        '''
        print('where you movin from')
        froom=input()
        print('where too')
        to=input()
        moves.append(f'{froom}{to}')'''
        bd=sf.get_best_move()
        moves.append(bd)
        board.push(chess.Move.from_uci(bd))
        print(type(bd))
        sf.set_position(moves)
        print(sf.get_board_visual())
        state=sf.get_evaluation()
        print(board)
        
        if sf.get_best_move()==None:
            #if state['type']=='mate' and state['value']==0:
            if board.is_stalemate():
                print('stalemate my dude white')
                play=False
                stalemate=stalemate+1
                continue
            if board.is_game_over()==True:
                print('mate my dude white')
                play=False
                white=white+1
                continue
            
            
        if board.is_fivefold_repetition()==True:
            print('5 fold')
            fold=fold+1
            #threeinrowdraw=True
            play=False
            continue
        if board.is_seventyfive_moves()==True:
            print('50 move')
            mov50=mov50+1
            #threeinrowdraw=True
            play=False
            continue
        n=n+1   
        bm=sf.get_best_move()
        moves.append(bm)
        sf.set_position(moves)
        print(sf.get_board_visual())
        board.push(chess.Move.from_uci(bm))
        state=sf.get_evaluation()
        print(state,sf.get_best_move())
        
        if sf.get_best_move()==None:
            #if state['type']=='mate' and state['value']==0:
            if board.is_stalemate():
                print('stalemate my dude black')
                play=False
                stalemate=stalemate+1
                continue
            if board.is_game_over()==True:
                print('mate my dude black')
                play=False
                black=black+1
                continue
        if board.is_fivefold_repetition()==True:
            print('5 fold')
            play=False
            fold=fold+1
            #threeinrowdraw=True
            continue
        if board.is_seventyfive_moves()==True:
            print('50 move')
            play=False
            mov50=mov50+1
            #threeinrowdraw=True
            continue
        n=n+1   
        print(board)
        if keyboard.is_pressed('w'):
            threeinrowdraw=True
            break
print(white,black,fold,mov50,stalemate,k)