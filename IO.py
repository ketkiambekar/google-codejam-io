#n_testcases = int(input())
n_testcases=1
output=[]

def count_right(game,player):
    #count consecutive Alphabets of player on right side
    count=0
    while len(game)>0 and game[-1]==player:
        game=game[:-1]
        count+=1
    return count

def count_left(game,player):
    #count consecutive Alphabets of player on left side
    count=0
    while len(game)>0 and game[0]==player:
        game=game[1:]
        count+=1
    return count

for t in range(n_testcases):
    #game=list(input())
    game=['I','O','I','O','O','O','I','I']
    original_game_length= len(game)
    turn = 0
    Score_I,Score_O=0,0
    
    #game loop
    while len(game)>0:
        #determine player
        player = 'I' if turn%2==0 else 'O'

        #game snapshot
        print(game, player)
        
        #compare consecutive letters from Left and right side
        R = count_right(game, player)
        L = count_left(game,player)
        

        if (L==0 and R==0) :
            len_game=len(game)

            if player=='O':
                output.append("Case #{}: {} {}".format((t+1), "I", Score_I+len_game))    
            if player=='I':
                output.append("Case #{}: {} {}".format((t+1), "O", Score_O+len_game))   
            break
        
        if R>0  :
            game = game[:-1]
         
        elif L>0:
            game = game[1:]
 

        if len(game)==0:
            if player=='I':
                output.append("Case #{}: {} {}".format((t+1), "I", 1))    
            if player=='O':
                output.append("Case #{}: {} {}".format((t+1), "O", 1))   
        turn+=1
        print(game, player, Score_I, Score_O)

#print output
for o in output:
    print(o)