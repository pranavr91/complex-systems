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

    def get_unique_id(self):
        """
        Helper method = generate Unique ID
        :return: unique id for the chromosome
        """
        try:
            ts = time.time()
            unique_id = hex(int(ts*10000000*random.randint(1,1000)))[2:]
            return unique_id
        except RuntimeError as rte:
            return str(rte)

    def impose_binary_schema(self,genome_seq):
        """
        Helper method - impose_binary_schema
        :param genome_seq: Gene sequence of the chromosome
        :return: modified genome sequence
        """
        try:
            for i in range(0,self.N):
                if (self.schema[i]==0 or self.schema[i]==1):
                    genome_seq[i] = self.schema[i]
            return genome_seq
        except IndexError as ie:
            print str(ie)

    def generate_binary_genome(self):
        """
        Generate binary genome - helper function
        :return: Genome sequence with randomly generated binary values
        """
        try:
            genome_sequence = [random.randint(1,1000)%2 for i in range(0,self.N)]
            if len(self.schema) > 0:
                genome_sequence = self.impose_binary_schema(genome_sequence)
            return genome_sequence
        except IndexError as ie:
            print str(ie)

    """
       Returns 0 if it is correct, else returns the error message.
    """
    def integer_genome_check(self):
        """
        Check if integer genome parameters are in correct format
        :return: 0 if integer genome is in correct format
                    error message otherwise
        """
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

    def impose_integer_schema(self,genome_seq):
        """
        Apply schema on the integer genome
        :param genome_seq: Integer genome sequence of the chromosome
        :return: Modified genome sequence with schema applied
        """
        try:
            for i in range(0,self.N):
                if isinstance(self.schema[i],int):
                    genome_seq[i] = self.schema[i]
            return genome_seq
        except IndexError as ie:
            print str(ie)

    def generate_integer_genome(self):
        """
        Method to generate random integer for genome sequence
        :return: Integer genome sequence
        """
        try:
            int_gen_chk = self.integer_genome_check()
            if int_gen_chk != 0:
                raise ValueError(int_gen_chk)
            genome_seq = [random.randint(self.range[i][0],self.range[i][1]) for i in range(0,self.N) ]
            if len(self.schema)>0:
                genome_seq = self.impose_integer_schema(genome_seq)
            return genome_seq
        except ValueError as ve:
            print str(ve)

    def generate_genome(self):
        """
        Intermediate method to generate a genome
        :return: binary,int,real or permutation genome
        """
        try:
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

    def print_chromosome(self):
        """
        Print function for debugging and general command line display
        :return: None
        """
        try:
            print '-' * 25
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
            print '-' * 25
        except Exception as e:
            print str(e)
            pass

    """method - Initial check
    Basic checks to ensure all the parameters are in proper format and type.
    Ensures dependencies between parameters are met.
    Parameters - N,name,schema,type,range
    Returns error message accordingly
    """
    def init_check(self,N,name,schema,type,range,elements):
        """
        Method to check if all parameters for the __init__ method are valid.
            -Checks if N is positive
            -Checks if Name is NOT empty
            -Makes sure schema length and genome length match
            -Makes sure type given is one among the known types
            -For int, real types, makes sure the range list matches length of genome
            - If type is perm, then an initial set of elements are required.

        :param N: Number of elements in the genome
        :param name: Name of the chromosome if any
        :param schema: An initial pattern that must be followed the chromosome irrespective of the randomness
        :param type: Type of chromosome - binary, int, real or permutation
        :param range: Range list containing tuples of the range in which the values can occur. Applies to int and real
        :param elements: Initial set of elements required for permutation type.
        :return: 0 if all checks are passed. Raises and returns the error if that is not the case
        """
        try:
            if (not isinstance(N,int)) or N <= 0:
                self.N = 0
                raise ValueError('N has to be a positive integer')
            if len(name) == 0:
                raise ValueError('Name cannot be empty')
            if len(schema) > 0 and len(schema) != N:
                raise ValueError('Schema length must match N (length of genome).')
            types = ['bin','int','real','perm']
            if type.lower() not in types:
                raise ValueError('Illegal value of type. Give bin,int,real or perm.')
            if type=='int' or type=='real' :
                if len(range) != N:
                    raise ValueError('Range length must match N (length of genome).')
            if type=='perm':
                    if len(elements)<=0:
                        raise ValueError('Elements cannot be empty when using Perm type')
            return 0
        except ValueError as ve:
            return ve

    def __init__(self, N=0, name='default', schema=[], type='bin', range_val=[],elements=[]):
        """
        Method to initialise a chromosome. Constructs the chromosome according to the parameters given
        :param N: Number of elements in the genome
        :param name: Name of the chromosome if any
        :param schema: An initial pattern that must be followed the chromosome irrespective of the randomness
        :param type: Type of chromosome - binary, int, real or permutation
        :param range_val: Range list containing tuples of the range in which the values can occur. Applies to int and real
        :param elements: Initial set of elements required for permutation type.
        """
        try:
            init_check = self.init_check(N, name, schema, type, range_val,elements)
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

"""
r = [(2, 10), (2, 10), (2, 10), (5, 15), (3, 20)]
sch= [5,4,'*','*','*']
c = Chromosome(N=5,schema=sch,type='int',range_val=r)
c.print_chromosome()

e = [1,2,3,4,5]
c=Chromosome(N=5,type='perm',elements=e)
c.print_chromosome()
"""