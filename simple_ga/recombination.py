from chromosome import Chromosome
import random
from mutation import mutation_flip_bit

LARGE_VALUE = 65536

def fitness_fn():
    return 1




def swap_at_index(ch1,ch2,index):
    try:
        temp = ch1.genome[index]
        ch1.genome[index] = ch2.genome[index]
        ch2.genome[index] = temp
        return ch1,ch2
    except IndexError as ie:
        print 'Index error has occured. No changes made.'
        return ch1,ch2




"""Recombination operator - 1-point recombination
Takes 2 chromosomes - 
Swaps values based on index
Returns new chromosomes
"""
def recombination_1_point(ch1,ch2,crossover_point=0):
    try:
        genome_length = len(ch1.genome)
        if crossover_point==0:
            crossover_point = random.randint(1,genome_length-1)
        #print 'Xover point...'+str(crossover_point)
        if crossover_point <= genome_length/2:
            for i in range(0,crossover_point):
                temp = ch1.genome[i]
                ch1.genome[i] = ch2.genome[i]
                ch2.genome[i] = temp
        else:
            for i in range(crossover_point,genome_length):
                ch1.genome[i], ch2.genome[i] = ch2.genome[i], ch1.genome[i]
        return ch1,ch2
    except IndexError:
        print 'Index error in chromosome.'

"""Recombination operator - 1-point recombination
Takes 2 chromosomes - 
Swaps values based on index
Returns new chromosomes
"""
def recombination_2_point(ch1,ch2,crossover_point_1=0,crossover_point_2=0):
    try:
        genome_length = len(ch1.genome)
        if crossover_point_1==0:
            a_val = random.randint(0,genome_length)
        if crossover_point_2==0:
            b_val = random.randint(0,genome_length)
        crossover_point_1 = min(a_val,b_val)
        crossover_point_2 = max(a_val,b_val)
        #print 'Xover point...'+str(crossover_point)
        for i in range(crossover_point_1, crossover_point_2):
            ch1.genome[i],ch2.genome[i] = ch2.genome[i],ch1.genome[i]

        """else:
            for i in range(crossover_point,genome_length):
                temp = ch1.genome[i]
                ch1.genome[i] = ch2.genome[i]
                ch2.genome[i] = temp"""
        return ch1,ch2
    except IndexError:
        print 'Index error in chromosome.'


"""Recombination operator - N-point recombination
Takes 2 chromosomes - 
Swaps values based for each index based on probability
Returns new chromosomes
"""
def recombination_n_point(ch1,ch2):
    try:
        for i in range(0, len(ch1.genome)):
            _choice = bool(random.getrandbits(1))
            if _choice:
                ch1.genome[i], ch2.genome[i] = ch2.genome[i], ch1.genome[i]
        return ch1,ch2
    except IndexError:
        print 'Index error in chromosome.'


"""
r = [(2, 10), (2, 10), (2, 10), (5, 15), (3, 20)]
c1 = Chromosome(N=5,type='int',range_val=r)
c2 = Chromosome(N=5,type='int',range_val=r)
c1.print_chromosome()
c2.print_chromosome()
c1,c2 = recombination_n_point(c1,c2)


c1.print_chromosome()
c2.print_chromosome()
"""

