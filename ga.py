class geneticModel:
   @staticmethod
   def rouletteSelcection(group):
      #perform selection

      return newgroup

   @staticmethod
   def truncatedSelcection(group):
      #perform selection
      return newgroup

   @staticmethod
   def tournamentSelcection(group):
      #perform selection
      return newgroup
      
   def __init__(randomIndividual, fitness, mutation, crossover, selection=None, populationSize=1000, mutationrate=0.05, parallelize=True):
      """Creates a new genetic algorithm model

      Keyword arguments:
      randomIndividual -- a function object which returns a random individual of class individualtype
      fitness          -- a function object which contains 
      mutation         -- a function object which accepts an individual and returns a new mutated version
      crossover        -- a function object which accepts two an
      selection        -- a function object which performs selection with predefined defaults
         Roulette Wheel Selection - rouletteSelection (Default)
         Truncated Selection      - truncatedSelection
         Tournament Selection     - tournamentSelection

      parallelize      -- a booleab to enable/disable parallelization(Defaults to True)
      """

      #Initialize Object variables
      self.randomIndividual = randomIndividual
      self.fitness = fitness
      self.mutation = mutation
      self.crossover = crossover
      self.selection = selection

      self.population = [individual for 



