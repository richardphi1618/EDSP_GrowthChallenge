ScoreCard_Options = ["ones", "twos", "threes", "fours", "fives", "sixes", "Three of a Kind", \
                        "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]


def Check(values, dice, CurrentScore):

    if values['ScoreOptions'][0] == "ones":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 1): points += dice[i]

        CurrentScore += points

    elif values['ScoreOptions'][0] == "twos":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 2): points += dice[i]

        CurrentScore += points   

    elif values['ScoreOptions'][0] == "threes":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 3): points += dice[i]

        CurrentScore += points 

    elif values['ScoreOptions'][0] == "fours":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 4): points += dice[i]

        CurrentScore += points 

    elif values['ScoreOptions'][0] == "fives":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 5): points += dice[i]

        CurrentScore += points  

    elif values['ScoreOptions'][0] == "sixes":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            if(dice[i] == 6): points += dice[i]

        CurrentScore += points  
    
    elif values['ScoreOptions'][0] == "Chance":
        print(f"player selected twos")
        points = 0

        for i in range(len(dice)):
            points += dice[i]

        CurrentScore += points     
    
    return CurrentScore