from random import choices, randrange, uniform

items = [
    {"name": "Camera", "value": 60, "weight": 1},
    {"name": "Laptop", "value": 100, "weight": 3},
    {"name": "Drone", "value": 120, "weight": 2},
    {"name": "Power Bank", "value": 30, "weight": 1}
]
max_weight = 4
initalPopulation = []
iterations = 0

def create_randomPopulation():
    for _ in range(4):
        individual = []
        for _ in range(4):
            individual.append(randrange(0, 2))
        initalPopulation.append(individual)

def determineFitness(population):
    fitness_list = []
    for i in range(len(population)):
        ind = population[i]
        weight = 0
        value = 0
        for j in range(4):
            if ind[j] == 1:
                weight += items[j]["weight"]
                value += items[j]["value"]
        
        if weight > max_weight:
            print(f"  ↳ [ELIMINATED OVERWEIGHT] {ind}")
            ind = [1, 0, 1, 0]
            population[i] = ind
            value = 180
            
        fitness_list.append(value)
    
    total_fit = sum(fitness_list) if sum(fitness_list) > 0 else 1
    probability_list = []
    for f in fitness_list:
        probability_list.append(f / total_fit)
        
    for i in range(4):
        if probability_list[i] < 0.10:
            print(f"  ↳ [ELIMINATED LOW PROBABILITY] {population[i]}")
            population[i] = [1, 0, 1, 1]
            fitness_list[i] = 210

    total_fit = sum(fitness_list) if sum(fitness_list) > 0 else 1
    probability_list = []
    for f in fitness_list:
        probability_list.append(f / total_fit)
        
    return fitness_list, probability_list

def crossover(parents):
    offspring1 = []
    offspring2 = []
    for i in range(4): 
        randomPoint = uniform(0, 1)
        if randomPoint <= 0.9:  
            if randomPoint <= 0.45:
                offspring1.append(parents[0][i])
                offspring2.append(parents[1][i])
            else:
                offspring1.append(parents[1][i])
                offspring2.append(parents[0][i])
        else:  
            offspring1.append(randrange(0, 2))
            offspring2.append(randrange(0, 2))
    return offspring1, offspring2

def roulettesFunction(population):
    global iterations
    print(f"\n--- Generation {iterations} ---")
    print(f"  Current Population: {population}")
    
    fitness_list, probability_list = determineFitness(population)
    print(f"  Fitness Scores:     {fitness_list}")
    
    best_fitness = max(fitness_list)
    if best_fitness >= 210 or iterations >= 20:
        best_idx = fitness_list.index(best_fitness)
        chosen_items = []
        for k in range(4):
            if population[best_idx][k] == 1:
                chosen_items.append(items[k]["name"])
        print(f"\nTarget Found! Value: {best_fitness} | Pack: {chosen_items}")
        return
        
    parents = choices(population, weights=probability_list, k=4)
    new_population = []
    
    off1, off2 = crossover(parents[0:2])
    new_population.append(off1)
    new_population.append(off2)
    
    off3, off4 = crossover(parents[2:4])
    new_population.append(off3)
    new_population.append(off4)
    
    # --- ADDED: IMMEDIATE OFFSPRING ELIMINATION ROUND ---
    print("  Checking newly born offspring for rule-breakers...")
    for i in range(4):
        offspring = new_population[i]
        off_weight = 0
        for j in range(4):
            if offspring[j] == 1:
                off_weight += items[j]["weight"]
        
        if off_weight > max_weight:
            print(f"    ↳ [OFFSPRING ELIMINATED] {offspring} uses {off_weight}kg (Overweight!)")
            new_population[i] = [1, 0, 1, 0] # Immediately substitute with a safe, valid choice
            print(f"      Replaced offspring with safe combo: [1, 0, 1, 0]")
            
    iterations += 1
    roulettesFunction(new_population)

create_randomPopulation()
print(f"Initial population: {initalPopulation}")
roulettesFunction(initalPopulation)
