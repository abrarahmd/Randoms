import random 

def breakdowninfo(info):
    breakbylines = info.split("\n")
    firstLine = breakbylines[0].split(" ")
    numBatsmen = int(firstLine[0])
    run_predicted = int(firstLine[1])
    batsman_runavg = []

    for i in range(1, len(breakbylines)):
        firstBatsman_secondRunavg = breakbylines[i].split(" ")
        batsman_runavg.append((firstBatsman_secondRunavg[0], int(firstBatsman_secondRunavg[1])))

    return numBatsmen, run_predicted, batsman_runavg

def select_populations(numBatsmen, batsman_runavg):
    populations = []
    binary = ["0", "1"]

    for i in range(numBatsmen):
        population = ""
        for j in range(numBatsmen):
            population += random.choice(binary)
        populations.append(population)

    fitnessList = []

    for i in range(len(populations)):
        fitnessList.append((fitness_function(populations[i], batsman_runavg)))

    selectedPopulations = []
    sorted_fitnessList = sorted(fitnessList)
    parent1Fitness = sorted_fitnessList[-1]
    parent2Fitness = sorted_fitnessList[-2]
    parent3Fitness = sorted_fitnessList[-3]
    index1 = None
    index2 = None
    index3 = None

    for i in range(len(fitnessList)):
        if fitnessList[i] == parent1Fitness:
            index1 = i
        if fitnessList[i] == parent2Fitness:
            index2 = i
        if fitnessList[i] == parent3Fitness:
            index3 = i

    selectedPopulations.append(populations[index1])
    selectedPopulations.append(populations[index2])
    selectedPopulations.append(populations[index3])

    return selectedPopulations

def fitness_function(check, batsman_runavg):
    fitness = 0

    for i in range(len(check)):

        if check[i] == "1":
            fitness += batsman_runavg[i][1]

    return fitness
    
def crossover_function(selectedPopulations):
    index = [0, 1, 2]
    mainPopulationindex = random.choice(index)
    mainPopulation = selectedPopulations[mainPopulationindex]
    sidePopulation1 = None
    sidePopulation2 = None

    for i in range(len(index)):
        if index[i] != mainPopulationindex:
            if sidePopulation1 == None:
                sidePopulation1 = selectedPopulations[index[i]]
            else:
                sidePopulation2 = selectedPopulations[index[i]]

    offspring1 = None
    offspring2 = None
    offspring3 = None
    offspring4 = None
    splitIndex = []

    for i in range(len(mainPopulation)):
        splitIndex.append(i)

    splitFrom = random.choice(splitIndex)
    offspring1 = mainPopulation[splitFrom:] + sidePopulation1[:splitFrom]
    offspring2 = sidePopulation1[splitFrom:] + mainPopulation[:splitFrom] 
    offspring3 = mainPopulation[splitFrom:] + sidePopulation2[:splitFrom]
    offspring4 = sidePopulation2[splitFrom:] + mainPopulation[:splitFrom]

    return offspring1, offspring2, offspring3, offspring4

def mutation_function(offspring1, offspring2, offspring3, offspring4):
    index = []
    binary = [0, 1]
    ofsprings = [offspring1, offspring2, offspring3, offspring4]

    for i in range(len(offspring1)):
        index.append(i)

    childrens = ["", "", "", ""]

    for i in range(len(ofsprings)):
        changeWith = str(random.choice(binary))
        changeIndex = random.choice(index)
        ofsprings[i] = list(ofsprings[i])
        ofsprings[i][changeIndex] = changeWith
        childrens[i] = ""
        
        for j in ofsprings[i]:
            childrens[i] += j
    
    return childrens[0], childrens[1], childrens[2], childrens[3]


def genetic_algorithm(numBatsmen, batsman_runavg, run_predicted):
    attempt = 0

    while True:
        selectedPopulations = select_populations(numBatsmen, batsman_runavg)
        offspring1, offspring2, offspring3, offspring4 = crossover_function(selectedPopulations)
        child1, child2, child3, child4 = mutation_function(offspring1, offspring2, offspring3, offspring4)
        child1_fitness =fitness_function(child1, batsman_runavg)
        child2_fitness =fitness_function(child2, batsman_runavg)
        child3_fitness =fitness_function(child3, batsman_runavg)
        child4_fitness =fitness_function(child4, batsman_runavg)

        if child1_fitness == run_predicted:
            return child1
            
        if child2_fitness == run_predicted:
            return child2

        if child3_fitness == run_predicted:
            return child3

        if child4_fitness == run_predicted:
            return child4
        
        if attempt >= 10000:
            return "-1"
        
        attempt += 1
            
file_path = 'E:/Courses/CSE422/Labs/Greedy Algorithm/input.txt'
with open(file_path, 'r') as file:
    info = file.read()

numBatsmen, run_predicted, batsman_runavg = breakdowninfo(info)
players = []

for i in batsman_runavg:
    players.append(i[0])

print(players)
print(genetic_algorithm(numBatsmen, batsman_runavg, run_predicted))