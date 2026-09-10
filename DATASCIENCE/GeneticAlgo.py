from random import choices,randrange,uniform

genes=["I","N","D","A"]
targetString = ["I", "N", "D", "I", "A"]
initialPopulation = []
n=4
iterations =0
def create_randomPopulation():
    global genes, initialPopulation, n
    for _ in range(n):
        random_choices =[]
        for _ in range (5):
            random_choices.append(randrange(0,4))

        individual=[]
        for i in range(len(random_choices)):
            individual.append(genes[random_choices[i]])

        initialPopulation.append(individual)
def determineFitness(population):
    global targetString
    print("Finding fitness and probability values for the population : ", population)
    fitness_list = []
    probability_list = []
    
    for i in population:
        fitness = 0
        for j in range(len(i)):
            if targetString[j] == i[j]:
                fitness += 1
        fitness_list.append(fitness)
        
    print("Fitness of the population is : ", fitness_list)
    denominator = sum(fitness_list)
    
    if denominator == 0:
        probability_list = [1/len(population)] * len(population)
    else:
        for i in range(len(fitness_list)):
            probability_list.append(fitness_list[i] / denominator)
            
    print("Probability of the population is : ", probability_list)
    return (fitness_list, probability_list)

def mutation():
    global genes
    random_mutationpoint1 = randrange(0, len(genes))
    return genes[random_mutationpoint1]

def crossover(parents):
    print("Parents for crossover are: ", parents)
    offspring1 = []
    offspring2 = []
    print("Generating offsprings...")
    
    for i in range(len(parents[0])):
        randomPoint = uniform(0, 1)
        if randomPoint <= 0.9:
            if randomPoint <= 0.45:
                offspring1.append(parents[0][i])
                offspring2.append(parents[1][i])
            else:
                offspring1.append(parents[1][i])
                offspring2.append(parents[0][i])
        else:
            offspring1.append(mutation())
            offspring2.append(mutation())
            
    print("offsprings from crossover and mutation of parents are : ", offspring1, offspring2, "\n")
    return offspring1, offspring2

def roulettesFunction(population):
    global iterations, n
    print("Iteration (Generation) : ", iterations)
    print("".center(90, "*"))
    fitness_list = []
    probability_list = []
    new_population = []
    
    fitness_list, probability_list = determineFitness(population)
    parents = choices(population, weights=probability_list, k=n)
    print("Fittest Parents selected with roulettes wheel from the population are : ", parents)
    print("\nGeneration new offsprings..........")
    
    offspring1, offspring2 = crossover(parents[0:2])
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    offspring1, offspring2 = crossover(parents[2:4])
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    print("The new generation after crossover and mutation is : ", new_population)
    
    if targetString in new_population:
        print("".center(90, "*"))
        print("Target string : INDIA found after ", iterations, " iterations (Generations).")
        print("".center(90, "*"))
        return
    else:
        print("\nTarget String not found...........")
        iterations += 1
        print("".center(90, "*"))
        roulettesFunction(new_population)
        return

create_randomPopulation()
print("Initial population is :", initialPopulation)
roulettesFunction(initialPopulation)