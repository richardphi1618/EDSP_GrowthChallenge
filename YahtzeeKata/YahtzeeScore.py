from collections import Counter


ScoreCard_Options = ["", "ones", "twos", "threes", "fours", "fives", "sixes", "Three of a Kind", \
                        "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))


def Check(values, dice, CurrentScore):

    #########################################################
    # Upper Section
    #########################################################
    for x in range(1,7):
        if values['ScoreOptions'][0] == ScoreCard_Options[x]:
            print(f"player selected {values['ScoreOptions'][0]}")
            points = 0

            for i in range(1,7):
                if(dice[i] == (x)): points += dice[i]
            
            CurrentScore += points     


    #########################################################
    # Lower Section
    #########################################################

    #Nothing Selected
    #TODO: Error Handling
    if values['ScoreOptions'][0] == ScoreCard_Options[0]:
        print("---ERROR---")

    #3 of a kind
    elif values['ScoreOptions'][0] == ScoreCard_Options[7]:
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0

        Count = Counter(dice)
        for i in range(6):
            if (Count[i+1] >= 3): 
                points = sum(dice)
                break

        CurrentScore += points     

    #4 of a Kind
    elif values['ScoreOptions'][0] == ScoreCard_Options[8]:
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0

        Count = Counter(dice)
        for i in range(6):
            if (Count[i+1] >= 4): 
                points = sum(dice)
                break

        CurrentScore += points    
    
    #Full House
    elif values['ScoreOptions'][0] == ScoreCard_Options[9]:
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0
        Check_3 = False
        Check_2 = False
        Count = Counter(dice)

        for i in range(1,7):
            if (Count[i] == 3): Check_3 = True
            if (Count[i] == 2): Check_2 = True
        
        if (Check_3 and Check_2):
            points = 25

        CurrentScore += points   

    #Straights
    elif values['ScoreOptions'][0] == ScoreCard_Options[10] or values['ScoreOptions'][0] == ScoreCard_Options[11] :
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0
        previous = 10
        count = 0

        #remove duplicates
        res = []
        for i in range(1,7):
            if dice[i] not in res:
                res.append(dice[i])
        
        if(len(res) >= 4 and checkConsecutive(res) and values['ScoreOptions'][0] == ScoreCard_Options[10]): points = 30
        if(len(res) >= 5 and checkConsecutive(res) and values['ScoreOptions'][0] == ScoreCard_Options[11]): points = 40

        CurrentScore += points   
    
    #Yahtzee
    elif values['ScoreOptions'][0] == ScoreCard_Options[12]:
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0

        if(all(x == dice[0] for x in dice)): points = 50

        CurrentScore += points    
 
    #Chance
    elif values['ScoreOptions'][0] == ScoreCard_Options[13]:
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0

        for i in range(1,7):
            points += dice[i]

        CurrentScore += points     
    
    return CurrentScore