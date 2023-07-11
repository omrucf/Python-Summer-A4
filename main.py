network = { # initializing the network
    'Omar': {'Jamie': 4, 'Heather': 8, 'Joshua': 4, 'Derek': 0, 'Bas': 0, 'Patrick': 2, 'Ray': 0, 'Bryan': 0, 'Rick': 2},
    'Jamie': {'Omar': 4, 'Heather': 9, 'Bas': 0},
    'Heather': {'Omar': 8, 'Jamie': 9, 'Joshua': 6, 'Derek': 2, 'Bas': 4},
    'Joshua': {'Omar': 4, 'Heather': 6, 'Bas': 0},
    'Derek': {'Omar': 0, 'Heather': 2},
    'Bas': {'Omar': 0, 'Jamie': 0, 'Heather': 4, 'Joshua': 0, 'Patrick': 7, 'Ray': 3, 'Bryan': 0, 'Rick': 3},
    'Patrick': {'Omar': 2, 'Bas': 7, 'Ray': 5},
    'Ray': {'Omar': 0, 'Bas': 3, 'Patrick': 5, 'Bryan': 0},
    'Bryan': {'Omar': 0, 'Bas': 0, 'Ray': 0, 'Rick': 3},
    'Rick': {'Omar': 2, 'Bas': 3, 'Bryan': 3}
}


def printFriends(network): # prints the friends of each person in the network
    for person in network: 
        friends = list(network[person].keys()) # gets the friends of the person
        print("\t{}'s:  {}".format(person, friends)) # prints the friends of the person


def printUniqueFOF(network): # prints the unique friends of friends of each person in the network
    for person in network: 
        fofs = set() # set of friends of friends to avoid duplicates
        friends = list(network[person].keys()) # gets the friends of the person
        for friend in friends: 
            for fof in network[friend]: # gets the friends of friends of the person
                if fof not in friends and fof != person: # if the friend of a friend is not a friend of the person and is not the person
                    fofs.add(fof) # add the friend of a friend to the set of friends of friends
        if len(fofs) == 0: # if the person has no unique friends of friends
            print("\t{} has no unique friends of friends".format(person)) 
        else: # if the person has unique friends of friends
            print("\t{}'s:  {}".format(person, list(fofs)))

def zeroCommincations(network): # prints the people who have never communicated
    visited = set() # set of visited pairs to avoid duplicates and to avoid checking the same pair twice
    for person in network: 
        for friend in network[person]: 
            if (person, friend) not in visited and (friend, person) not in visited: # if the pair has not been visited
                visited.add((person,friend)) # add the pair to the set of visited pairs
                if network[person][friend] == 0: # if the person and friend have never communicated
                    print("\t\u2022 {} and {}".format(person, friend)) # print the pair

def avgNumOfFriends(network): # returns the average number of friends
    total = 0 
    for person in network: 
        total += len(network[person]) # adds the number of friends of each person to the total
    return total / len(network) # returns the average number of friends

def moreThanFourFriends(network): # prints the people who have more than four friends
    for person in network:
        if len(network[person]) > 4: # if the person has more than four friends
            print("\t\u2022 {}".format(person)) # print the person


def main(): # main function
    print("friends in network:") 
    printFriends(network) 
    print("\nunique friends of friends in network:")
    printUniqueFOF(network)
    print("\npeople who have never communicated:")
    zeroCommincations(network)
    print("\naverage number of friends:", end=" ")
    print(avgNumOfFriends(network))
    print("\npeople with more than four friends:")
    moreThanFourFriends(network)

main()
# Omar Yossuf
# 900212166
# 11th of July 2023