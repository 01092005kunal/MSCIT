from random import choices, randrange, uniform

items = [
    {"name": "Camera", "value": 60, "weight": 1},
    {"name": "Laptop", "value": 100, "weight": 3},
    {"name": "Drone", "value": 120, "weight": 2},
    {"name": "Power Bank", "value": 30, "weight": 1}
]
max_weight = 4
num_items = len(items)

initalPopulation = []
n = 4
iterations = 0

def create_randomPopulation():
    global initalPopulation, n, num_items
    for _ in range(n):
        individual = []
        for _ in range(num_items):
            individual.append(randrange(0, 2))  
        initalPopulation.append(individual)

def determineFitness(population):
    global items, max_weight
    print("Finding fitness values for the population : ", population)
    fitness_list = []
    probability_list = []
    
    for individual in population:
        total_value = 0
        total_weight = 0
        for j in range(len(individual)):
            if individual[j] == 1:
                total_value += items[j]["value"]
                total_weight += items[j]["weight"]
        
        if total_weight > max_weight:
            fitness = 0  
        else:
            fitness = total_value
        fitness_list.append(fitness)
        
    print("Fitness (Total Value) of the population is : ", fitness_list)
    denominator = sum(fitness_list)
    
    if denominator == 0:
        probability_list = [1/len(population)] * len(population)
    else:
        for i in range(len(fitness_list)):
            probability_list.append(fitness_list[i] / denominator)
            
    print("Selection Probability of the population is : ", probability_list)
    return (fitness_list, probability_list)

def mutation():
    return randrange(0, 2)

def crossover(parents):
    print("Parents selected for crossover are: ", parents)
    offspring1 = []
    offspring2 = []
    
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
            
    return offspring1, offspring2

def roulettesFunction(population):
    global iterations, n
    print("\n" + f" Generation {iterations} ".center(90, "*"))
    
    fitness_list, probability_list = determineFitness(population)
    parents = choices(population, weights=probability_list, k=n)
    print("Parents selected via Roulette Wheel: ", parents)
    
    new_population = []
    offspring1, offspring2 = crossover(parents[0:2])
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    offspring1, offspring2 = crossover(parents[2:4])
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    print("New Generation population: ", new_population)
    
    best_fitness = max(fitness_list)
    if best_fitness >= 210 or iterations >= 20:
        print("\n" + "".center(90, "*"))
        if best_fitness >= 210:
            best_idx = fitness_list.index(best_fitness)
            best_combo = population[best_idx]
            chosen_items = [items[k]["name"] for k in range(len(best_combo)) if best_combo[k] == 1]
            print(f"Optimal Solution Found: Value of {best_fitness} reached!")
            print(f"Pack the following items: {chosen_items}")
        else:
            print("Reached termination limit (20 generations).")
        print("".center(90, "*"))
        return
    else:
        iterations += 1
        roulettesFunction(new_population)
        return

create_randomPopulation()
print("Initial random choices (0=Exclude, 1=Include): ", initalPopulation)
roulettesFunction(initalPopulation)
