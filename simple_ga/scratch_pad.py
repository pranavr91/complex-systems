import random
"""
#g = [random.randint(1,1000)%2 for i in range(0,10)]
#print g

a = (5,6)
print a
l = []
l.append(a)
b = (2,3)
l.append(b)
print l

c=4
print c.__class__
t = type(b).__name__
print t
#if str(t) == 'tuple':
#    print 'yes'


a=4
b=6
s = [1,2,3]
s[a<b]=1
s[a>b]=-1
print s


a=1
b=1
print a^b
"""
from mutation import mutation_flip_bit
from chromosome import Chromosome
from selection import random_chromosome_selection

c1 = Chromosome(N=10)
c2 = Chromosome(N=10)
c3 = Chromosome(N=10)
c4 = Chromosome(N=10)
c5 = Chromosome(N=10)
population = [c1,c2,c3,c4,c5]
for i in population:
    i.print_chromosome()
pop = random_chromosome_selection(population)
print '*'*100
print len(pop)
for i in pop:
    i.print_chromosome()
"""
c1.print_chromosome()
c1 = mutation_flip_bit(c1,probability=0.7)
c1.print_chromosome()
"""