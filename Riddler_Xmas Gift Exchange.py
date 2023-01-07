import random # imports the random module in order to make random selections from lists

results = [] # list of results
counter = 0 # counts number of trials

while counter < 250000: # number of trials set to 250,000

    family = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q,', 'r', 's', 't'] # list of participants
    hat = [] # list from which the names are drawn
    draws = [] # list to log the draws for each round
    pairs = [] # list to log the pairs for each round
    rounds = 0 # counts number of rounds it takes to pair up all of the family members

    while len(family)>0: # perform the below function until the list of participants is empty

        for x in family: # for each participant in the family list
            newlist = [y for y in family if y != x] # generate a new list of available family members excluding themself
            z = random.choice(newlist) # draw a random name from the new list
            hat.append(z) # add that name to the hat; repeat for each member still in the family list
        random.shuffle(family) # shuffle the family list
        for x in family: # for each participant in the family list
            draw = random.choice(hat) # draw a random name from the hat
            hat.remove(draw) # remove that name from the hat
            pair = [x, draw] # create a sublist containing the family member and their draw
            pair.sort() # sort the sublist alphabetically - it will help to identify pairs later
            draws.append(pair) # append the sublist to the draws log

        # this procedure identifies pairs
        for x in draws: # for each list of family members and their draw
            if draws.count(x) == 2: # if there are two identical sublists of the family member and their draw
                if x not in pairs: # if the list of family members and their draw isn't already logged in the pairs list
                    pairs.append(x) # append the pair to the pairs list
                    family.remove(x[0]) # remove the first member of the pair from the family members list
                    family.remove(x[1]) # remove the second member of the pair from the participant from the family members list
        draws = [] # clear the draws log for the next round
        hat = [] # clear the hat for the next round
        rounds = rounds+1 # log one round to the round counter
        

    results.append(rounds) # log the number of rounds to a results list
    counter = counter+1 # logs one complete trial to the trial counter

# once the number of complete trials reaches 250,000, the average number of trials will be printed to the terminal

print ("The average number of rounds needed in" , counter , "trials is " , sum(results)/len(results))