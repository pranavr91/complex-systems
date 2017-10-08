"""Mutation operators for simple genetic algorithm
"""
import random

def mutation_flip_bit(ch,probability=0.5):
    """

    :param ch: Chromosome - will mutate the chromosome at random
    :return: Chromosome after modification
    """
    try:
        if probability > 1:
            raise ValueError('Probability of mutation value cannot be greater than 1.')
        if probability <0:
            raise ValueError('Probability of mutation cannot be less than zero')
        _toss = random.randint(0,100)/100.0
        print _toss
        if _toss < probability:
            _flip = random.randint(0,len(ch.genome))
            print _flip
            ch.genome[_flip] = ch.genome[_flip]^1
        return ch
    except ValueError as ve:
        print str(ve)



