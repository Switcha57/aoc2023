from functools import lru_cache
from functools import cmp_to_key
pCards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']

def DrawBreak(hands_1,hands_2) ->int:
    ret = True
    for i,j in zip(hands_1,hands_2):
        if pCards.index(i)>pCards.index(j): #if second card is ofg higher value return false
            return -1
        elif pCards.index(i)<pCards.index(j):
            return 1
    return 0

@lru_cache
def countCard(hand):
    value_counts = {}
    for card in hand:
        if card in value_counts:
            value_counts[card] += 1
        else:
            value_counts[card] = 1
    if 'J' in value_counts:
        jolly = value_counts['J']
        value_counts['J']=0
        value_counts[max(value_counts, key=value_counts.get)]+=jolly
    return value_counts

def is_five_of_a_kind(hand):
    # Count the occurrences of each card value in the hand
    value_counts = countCard(hand)
    
    # Check if any card value occurs five times
    for count in value_counts.values():
        if count == 5:
            return True
    return False

def is_four_of_a_kind(hand):
    # Count the occurrences of each card value in the hand
    value_counts = countCard(hand)
    
    # Check if any card value occurs four times
    for count in value_counts.values():
        if count == 4:
            return True
    return False

def is_full_house(hand):
    # Count the occurrences of each card value in the hand
    value_counts= countCard(hand)
    
    # Check for a full house: one value occurring three times and another occurring twice
    has_three_of_a_kind = False
    has_pair = False
    for count in value_counts.values():
        if count == 3:
            has_three_of_a_kind = True
        elif count == 2:
            has_pair = True
    
    return has_three_of_a_kind and has_pair
def is_three_of_a_kind(hand):
    # Count the occurrences of each card value in the hand
    value_counts = countCard(hand)
    
    # Check if any card value occurs three times
    for count in value_counts.values():
        if count == 3:
            return True
    return False

def is_two_pair(hand):
    # Count the occurrences of each card value in the hand
    value_counts = countCard(hand)
    
    # Check for two pairs
    pairs = 0
    for count in value_counts.values():
        if count == 2:
            pairs += 1
    
    return pairs == 2
def is_one_pair(hand):
    # Count the occurrences of each card value in the hand
    value_counts = countCard(hand)
    
    # Check for a single pair
    for count in value_counts.values():
        if count == 2:
            return True
    return False
def RankHand(hand):
    rank = -1
    if is_five_of_a_kind(hand):
        rank=5
    elif is_four_of_a_kind(hand):
        rank = 4
    elif is_full_house(hand):
        rank = 3
    elif is_three_of_a_kind(hand):
        rank= 2
    elif is_two_pair(hand):
        rank = 1
    elif is_one_pair(hand):
        rank = 0
    return rank

def compare(game_1,game_2):
    hand_1=game_1[0]
    hand_2=game_2[0]
    if(RankHand(hand_1)<RankHand(hand_2)):
        return -1
    elif RankHand(hand_1)>RankHand(hand_2):
        return 1
    else:
        return DrawBreak(hand_1,hand_2)
        
    

game=[]
with open("7/input","r") as inputFile:
    for line in inputFile:
        _=line.split()
        game.append((_[0],int(_[1])))
risp = 0
f=sorted(game,key=cmp_to_key(compare))
for i in range(0,len(f)):
    risp+=((i+1)*f[i][1])
    
print ( risp)