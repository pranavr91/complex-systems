import unittest
from .. import chromosome as C


class ChromosomeTest(unittest.TestCase):

    """Unit Tests for Chromosome class and associated methods
    """
    """Test 1
    - See if chromosome length matches input size
    """
    def test_case_bin_chromosome_length_positive(self):
        N = 50
        ch = C.Chromosome(N)
        N_assert = 50
        len_assert = 50
        self.assertEquals(ch.N,N_assert)
        self.assertEquals(len(ch.genome),len_assert)

    """Test 2
        - See chromosome state for invalid chromosome length
    """
    def test_case_bin_chromosome_length_not_valid(self):
        N = -6
        ch = C.Chromosome(N)
        N_assert = 0
        self.assertEquals(ch.N, N_assert)

    """Test 3
        - See if chromosome length matches input size
    """
    def test_case_bin_chromosome_length_not_num(self):
        N = "Nval"
        ch = C.Chromosome(N)
        N_assert = 0
        self.assertEquals(ch.N, N_assert)


    """Test 4
        - See if chromosome generates unique ID
    """
    def test_case_bin_chromosome_unique_id_check(self):
        N=40
        ch1 = C.Chromosome(N)
        ch2 = C.Chromosome(N)
        self.assertNotEquals(ch1.ID,ch2.ID)


    """Test 5
    For an int chromosome - see if all the integer values fall into the range specified
    """
    def test_case_int_chromosome_range_restrict(self):
        range2 = [(2, 10), (2, 10), (2, 10), (5, 15), (3, 20)]
        c = C.Chromosome(N=5, type='int', name='int_pop', range=range2)
        result = True
        for i in range(0,c.N):
            if c.genome[i]>=c.range[i][0] and c.genome[i]<=c.range[i][1]:
                result = True
            else:
                result=False
                break
        self.assertEquals(result, True)


    """Test 6
       For an int chromosome - see if all the tuples in the range are in correct format
       """
    def test_case_int_chromosome_range_wrong_tuple_format(self):
        range2 = [(2, 10), (2, 10), (10, 2), (5, 15), (3, 20)]
        c = C.Chromosome(N=5, type='int', name='int_pop', range=range2)
        result = True
        self.assertEquals(c.genome, None)








if __name__ == '__main__':
    unittest.main()