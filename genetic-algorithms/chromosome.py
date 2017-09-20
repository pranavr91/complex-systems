"""
Class file -
Contains Chromosome class. Basic structure of a genetic algorithm

class - Chromosome
Methods - __init__
          init_check
          generate_genome
          print_chromosome
          generate_unique_id
          impose_binary_schema
          generate_binary_genome
          generate_integer_genome


AUTHOR - Pranav R.
"""

import random
import time



class Chromosome(object):

    """Chromosome class
    init Parameters - N - number of genes
                ID - ID assigned for each chromosome (String)
                population - name of the population to which chromosome belongs (optional)
                schema - If a schema is given, then schema is imposed on every chromosome. (List)
                Genome - the gene sequence of the chromosome. Can be binary values or real numbers or integers
                type - type of chromosome needed - can be binary(bin),real(real),integer values(int),permutation(perm). Default is binary values
                Fitness - Fitness of the chromosome is calculated and stored during iterations
                Range = range of values - applies if type is range or real
    """

    """Helper method = generate Unique ID
    Takes no parameter. Returns ID string
    """
    def get_unique_id(self):
        try:
            ts = time.time()
            unique_id = hex(int(ts*10000000*random.randint(1,1000)))[2:]
            return unique_id
        except RuntimeError as rte:
            return str(rte)


    """
    Helper method - impose_binary_schema
    -Takes genome_sequence and schema
    -Return genome sequence
    """
    def impose_binary_schema(self,genome_seq):
        try:
            for i in range(0,self.N):
                if (self.schema[i]==0 or self.schema[i]==1):
                    genome_seq[i] = self.schema[i]

            return genome_seq
        except IndexError as ie:
            print str(ie)


    """Generate binary genome - helper function
    Returns list - genome sequence
    Parameters - N, schema
    """
    def generate_binary_genome(self):
        try:
            genome_sequence = [random.randint(1,1000)%2 for i in range(0,self.N)]
            if len(self.schema) > 0:
                genome_sequence = self.impose_binary_schema(genome_sequence)
            return genome_sequence
        except IndexError as ie:
            print str(ie)


    """Check if integer genome parameters are in correct format
       Returns 0 if it is correct, else returns the error message.
    """
    def integer_genome_check(self):
        try:
            for i in self.range:
                if type(i).__name__ != 'tuple':
                    raise ValueError('All entries in range must be tuples - (lower_value,higher_value).')
                if i[0]>=i[1]:
                    raise ValueError('The tuples in the range must be of the form - (lower_value,higher_value). '
                                     'It appears that is not the case in '+(str(i)))
            return 0
        except ValueError as e:
            return e


    """generate integer genome - helper function
    returns list - integer genome sequence
    Parameter - N,schema,range of int values for each field. 
    """
    def generate_integer_genome(self):
        try:
            int_gen_chk = self.integer_genome_check()
            if int_gen_chk != 0:
                raise ValueError(int_gen_chk)
            genome_seq = [random.randint(self.range[i][0],self.range[i][1]) for i in range(0,self.N) ]
            return genome_seq
        except ValueError as ve:
            print str(ve)


    """Method - initialize Genome of chromosome
       Returns - list i.e. the genome sequence
       Parameters - N, schema, type
    """
    def generate_genome(self):
        try:
            #genome = []
            if isinstance(self.N, int):
                if self.N <= 0:
                    return []
                if self.type == 'bin':
                    return self.generate_binary_genome()
                elif self.type == 'int':
                    return self.generate_integer_genome()
            else:
                raise ValueError('N must be an integer.')

        except ValueError as value_error:
            print str(value_error)


    """
    Chromosome - print function
    Prints the contents of a chromosome 
    -takes no argument
    """
    def print_chromosome(self):
        try:
            print '---Chromosome Details---'
            print '-'*25
            print 'ID :' + self.ID
            print 'Population :'+self.population
            print 'Size :'+str(self.N)
            print 'Type :'+self.type
            print 'Genome sequence:'
            print self.genome
            print 'Fitness value :'+str(self.fitness)
            print 'Schema :'+str(self.schema)

        except Exception as e:
            print str(e)
            pass

    """method - Initial check
    Basic checks to ensure all the parameters are in proper format and type.
    Ensures dependencies between parameters are met.
    Parameters - N,name,schema,type,range
    Returns error message accordingly
    """
    def init_check(self,N,name,schema,type,range):
        try:
            if (not isinstance(N,int)) or N <= 0:
                self.N = 0
                raise ValueError('N has to be a positive integer')
            if len(name) == 0:
                raise ValueError('Name cannot be empty')
            if len(schema) > 0 and len(schema) != N:
                raise ValueError('Schema length must match N (length of genome).')

            types = ['bin','int','real','perm']
            if type not in types:
                raise ValueError('Illegal value of type. Give bin,int,real or perm.')
            if type=='int' or type=='real' or type=='perm':
                if len(range) != N:
                    raise ValueError('Range length must match N (length of genome).')
            return 0
        except ValueError as ve:
            return ve


    """Init docs - see class Docs"""
    def __init__(self, N=0, name='default', schema=[], type='bin', range_val=[]):
        try:
            init_check = self.init_check(N, name, schema, type, range_val)
            if init_check != 0:
                raise ValueError('ERROR: '+str(init_check))

            self.population = name
            self.ID = self.get_unique_id()
            self.N = N
            self.fitness = 0
            self.schema = schema
            self.type = type
            self.range = range_val
            self.genome = self.generate_genome()
        except ValueError as v:
            print str(v)


#sch = [1,0,'*','*','*','*','*',0,0,'*']
#range2 = [(2,10),(2,10),(1,10),(5,15),(3,20)]
#c = Chromosome(N=5,type='int',name='int_pop',range=range2)
#c.print_chromosome()

#c.print_chromosome()
#print c.get_unique_id()
#print g