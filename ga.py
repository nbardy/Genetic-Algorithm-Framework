import random
import bisect

class geneticModel:
   @staticmethod
   def rouletteSelection(group, fitnessFunc):
      """
      Implements Roulette Wheel Selection
      """

      fitnessDistribution = _getDistribution(map(fitnessFunc, group))
      #create of map of distributions to individuals
      return _getPairs(group, fitnessDistribution)

   @staticmethod
   def rankSelection(group, fitnessFunc):
      """
      Implements Rank Selection
      """
      rankedGroup = sorted(group, lambda x,y: cmp(fitnessFunc(x),fitnessFunc(y)))
      
      #Can be optimized with (n+1)*n/2
      distribution = _getDistribution(range(1, len(group) + 1))
      
      return _getPairs(rankedGroup, distribution)

   @staticmethod
   def truncatedSelection(group, fitnessFunc):
      #perform selection

      return newgroup

   @staticmethod
   def tournamentSelection(group, fitnessFunc):
      #perform selection

      return newgroup

   def __init__(self, randomIndividual, fitness, mutation, crossover, selection=None, populationSize=1000, mutationRate=0.05):
      """Creates a new genetic algorithm model

      Keyword arguments:
      randomIndividual -- a function object which returns a random individual
      fitness          -- a function object which accepts an individual, and returns a fitness score 
      mutation         -- a function object which accepts an individual, and mutation rate returns an individual
      crossover        -- a function object which accepts a tuple of size 2 and returns a single individual
      selection        -- a function object which accepts a populaion and a fitness function and returns a population of the same size
         Roulette Wheel Selection - rouletteSelection (Default)
         Truncated Selection      - truncatedSelection
         Tournament Selection     - tournamentSelection
      """

      #Initialize Object variables
      self.randomIndividual = randomIndividual
      self.fitness = fitness
      self.mutation = mutation
      self.crossover = crossover
      self.populationSize = populationSize
      self.mutationRate = mutationRate

      if selection == None:
         selection = geneticModel.rouletteSelection
      self.selection = selection

      #Create initial population
      self.population = [self.randomIndividual() for i in xrange(populationSize)]

   def advanceGeneration(self):
      """
      Advances the genetic Model one generation
      """
      #Use given selection technique for selecting parents
      parents = self.selection(self.population, self.fitness)

      #Create a child and mutate for every pair of parents
      newgeneration = [self.mutation(self.crossover(pair), self.mutationRate) for pair in parents]
      
      self.population = newgeneration

def _getDistribution(valueList):
   """
   Accepts a list of values and returns a distribution
   
   Example: [.3, .4, .11, .09, .03, .07] => [.3, .7, .81, .90, .93, 1]
            [4, 5, 5, 6]                 => [.2, .45, .70, 1]
   """
   totalValue = sum(valueList)
   densityList = [value/float(totalValue) for value in valueList]
   cumValue = 0
   distributionList = []

   for value in densityList:
      cumValue = cumValue + value
      distributionList.append(cumValue)

   return distributionList

def randomFromDistribution(distribution):
   """
   Accepts a distribution and returns an integer representing the selected index
   """
   return bisect.bisect(distribution, random.random())

def _getPairs(group, fitnessDistribution):
   selectionGroup = [ ]
   for _ in range(len(group)):
      selectionGroup.append( ( group[randomFromDistribution(fitnessDistribution)], 
                               group[randomFromDistribution(fitnessDistribution)] ))
   return selectionGroup
