from pprint import pprint

with open("4\input","r") as inputFile:
    gameId = 1
    
    num_Scratch=[1]*224 #inputSIze
    num_Scratch[0]=0
    for singleLine in inputFile:
        curr=0
        game = ((singleLine.split(":"))[1]).split("|")
        winningHand=set()
        myGame=set()
        game[0]=game[0].strip()
        game[1]=game[1].strip()
       # pprint(game[1].split(" "))
        #pprint([int(v) for v in game[0].split(" ")])
        winningHand.update([int(v) for v in filter(lambda a: a != "",  game[0].split(" "))])
        myGame.update([int(v) for v in filter(lambda a: a != "",  game[1].split(" "))])
        next_won=1
        for i in winningHand:
            if i in myGame:
                num_Scratch[gameId+next_won]=num_Scratch[gameId+next_won]+num_Scratch[gameId]
                next_won+=1
        
        gameId +=1
    print(sum(num_Scratch))