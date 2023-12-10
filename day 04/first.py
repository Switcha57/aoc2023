from pprint import pprint

with open("4\input","r") as inputFile:
    # gameId not usefull
    risp=0
    for singleLine in inputFile:
        curr=0
        game = ((singleLine.split(":"))[1]).split("|")
        #pprint(game)
        winningHand=set()
        myGame=set()
        game[0]=game[0].strip()
        game[1]=game[1].strip()
       # pprint(game[1].split(" "))
        #pprint([int(v) for v in game[0].split(" ")])
        winningHand.update([int(v) for v in filter(lambda a: a != "",  game[0].split(" "))])
        myGame.update([int(v) for v in filter(lambda a: a != "",  game[1].split(" "))])
        for i in winningHand:
            if i in myGame:
                curr = 1 if curr==0 else curr*2
        risp+=curr
    print(risp)