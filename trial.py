#To handle reloads in python interpreter
try:
   reload(ga)
except:
   import ga

import random
import math

# f(x) = x**2 - 12*x + 7 for x= [0,30]
model1 = ga.geneticModel( randomIndividual = lambda: random.randint(1,5),
                          fitness          = lambda x: x**2 - 12*x + 7,
                          mutation         = lambda x, mutationrate: max(min( x + random.normalvariate(0,5), 30),0),
                          crossover        = lambda (x,y): (x + y) /2,
                          selection        = ga.geneticModel.rouletteSelection)

# eval string of 1's and 0's
# For large size this model has a exponentially slower convergence with roulette selection. Shows a good use case for rank selection over roulette
size = 100
model2 = ga.geneticModel( randomIndividual = lambda: ''.join([str(random.randint(0,1)) for _ in range(size)]),
                          fitness          = lambda x: int(x, 2),
                          mutation         = lambda x, mutationrate: ''.join(map(lambda bit: str(int(bit)^int(math.ceil(mutationrate - random.random()))), x)),
                          crossover        = lambda (x,y): (lambda index: x[:index] + y[index:])(random.randint(0,len(x))),
                          selection        = ga.geneticModel.rankSelection)


