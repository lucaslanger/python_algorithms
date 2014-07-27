def readData():
    with open("knapsackData.text") as f:
        data = []
        firstline = True
        for line in f:
            if firstline:
                firstline = False
            else:
                data.append([int(i) for i in line.split(' ')])
        
    return data

def knapsack(backpackweight, choice_index, choices, computed =[[0 for j in range(choice_index)] for i in range(backpackweight)]):
    lastval = choice[choice_index]
    solution = max( knapsack(backpackweight, choice_index-1, choices, computed),
                    knapsack(backpackweight-lastval[0], choice_index-1, choices, computed + lastval[1] ) )
    
    computed[backpackweight][choice_index] = solution
    return solution