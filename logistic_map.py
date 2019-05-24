import matplotlib.pyplot as plt
from math import log

# TODO - Color based on probability mass
# TODO - Show temperature/entropy as background color
# TODO - https://en.wikipedia.org/wiki/List_of_chaotic_maps 


# entropy coloring stable 100-800 generations_to_plot
COLOR_MAP = {.04: 'violet', .13: 'red', .25: 'pink', .5: 'orange', 1:'blue'}
def COLOR(x):
    for key, value in COLOR_MAP.items():
        if x <= key:
            return value

    return 'black'


NORM_FACTOR = .001
def NORMALIZE(x):
    if NORM_FACTOR == 0:
        return x

    return x // NORM_FACTOR * NORM_FACTOR


if __name__ == '__main__':
    # Setup
    RULE = lambda x: r * x * (1-x)

    USE_ENTROPY = True  # Measure entropy or temperature by color

    MIN = 0            # Min r
    MAX = 4            # Max r
    GRANULARITY = 500  # Slices per unit r

    GENERATIONS = 2000 # Times population is recalculated
    GENERATIONS_TO_PLOT = int(.1 * GENERATIONS)

    # Calculate
    X = []             # r
    Y = []             # population
    Z = []             # entropy or temperature
    for r in (MIN + (i / GRANULARITY) for i in range((MAX-MIN) * GRANULARITY)):
        # Initialize
        populations = [.5]
        if GENERATIONS == GENERATIONS_TO_PLOT:
            X.append(r)
            Y.append(NORMALIZE(populations[-1]))  

        # Calculate Y
        for g in range(len(populations), GENERATIONS):
            population = max(0, RULE(populations[-1]))
    
            populations.append(population)

            if g >= GENERATIONS - GENERATIONS_TO_PLOT:
                X.append(r)
                Y.append(NORMALIZE(population))  

        # Calculate Z
        sample = Y[-GENERATIONS_TO_PLOT:]

        probability_mass = {v: 1 / sample.count(v) for v in set(sample)}

        temperature = len(set(sample))
        entropy = - sum([x * log(x) for x in probability_mass.values()])

        color = COLOR(1 / (1 + entropy) if USE_ENTROPY else 1 / temperature)
        
        Z += [color] * GENERATIONS_TO_PLOT
        
    # Plot
    plt.scatter(X, Y, c=Z, s=.1)
    
    plt.gcf().canvas.set_window_title('Bifurication Diagram')
    plt.title('Logistic Map')
    plt.xlabel('Replacement Rate')
    plt.ylabel('Population / Carrying Capacity')
    plt.legend(['Entropy' if USE_ENTROPY else 'Temperature'])
    
    plt.show()
