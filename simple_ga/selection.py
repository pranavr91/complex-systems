import random

def random_chromosome_selection(population,max_copies=2):
    try:
        new_population = [random.choice(population) for i in xrange(0,len(population))]
        return new_population
        """
        temp_pop = population
        new_population = []
        old_pop_size = len(temp_pop)
        while(len(new_population) < old_pop_size):
            _copies = random.randint(0,max_copies)
            _index = random.randint(0, len(temp_pop)-1)
            #print _index
            _chromosome = temp_pop[_index]
            for i in range(0,max_copies):
                new_population.append(_chromosome)
            temp_pop.remove(temp_pop[_index])
        random.shuffle(new_population)
        return new_population[0:old_pop_size]
        """
    except IndexError as ie:
        print str(ie)
    except:
        print 'Exception has occured..'




