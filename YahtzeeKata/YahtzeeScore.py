from collections import Counter


ScoreCard_Options = ["ones", "twos", "threes", "fours", "fives", "sixes", "Three of a Kind", \
                        "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]


def Check(values, dice, CurrentScore):

    for x in range(6):
        if values['ScoreOptions'][0] == ScoreCard_Options[x]:
            print(f"player selected {values['ScoreOptions'][0]}")
            points = 0

            for i in range(len(dice)):
                if(dice[i] == (x+1)): points += dice[i]
            
            CurrentScore += points     
    
    if values['ScoreOptions'][0] == "Yahtzee":
        print(f"player selected {values['ScoreOptions'][0]}")
        points = 0

        if(all(x == dice[0] for x in dice)): points = 50

        CurrentScore += points     

    elif values['ScoreOptions'][0] == "Three of a Kind":
        print(f"player selected twos")
        points = 0

        Count = Counter(dice)
        for i in range(len(dice)):
            if (Count[i] >= 3): 
                points = sum(dice)
                break

        CurrentScore += points     

    elif values['ScoreOptions'][0] == "Four of a Kind":
        print(f"player selected twos")
        points = 0

        Count = Counter(dice)
        for i in range(len(dice)):
            if (Count[i] >= 4): 
                points = sum(dice)
                break

        CurrentScore += points    
    
    elif values['ScoreOptions'][0] == "Full House":
        print(f"player selected twos")
        points = 0
        Check_3 = False
        Check_2 = False
        Count = Counter(dice)
        
        for i in range(len(dice)):
            if (Count[i] == 3): Check_3 = True
            if (Count[i] == 2): Check_2 = True
            if (Check_3 and Check_2):
                points = 25
                break

        CurrentScore += points   
 
    elif values['ScoreOptions'][0] == "Chance":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            points += dice[i]

        CurrentScore += points     
    
    return CurrentScore