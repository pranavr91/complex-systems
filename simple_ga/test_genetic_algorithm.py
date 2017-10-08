import unittest
import chromosome as C
from recombination import recombination_1_point

class ChromosomeTest(unittest.TestCase):

    """Unit Tests for Chromosome class and associated methods
    """

    def test_case_bin_chromosome_length_positive(self):
        """
        Test 1
        - See if chromosome length matches input size
        :return: None
        """
        N = 50
        ch = C.Chromosome(N)
        N_assert = 50
        len_assert = 50
        self.assertEquals(ch.N,N_assert)
        self.assertEquals(len(ch.genome),len_assert)

    def test_case_bin_chromosome_length_not_valid(self):
        """
        Test 2
        - See chromosome state for invalid chromosome length
        :return: None
        """
        N = -6
        ch = C.Chromosome(N)
        N_assert = 0
        self.assertEquals(ch.N, N_assert)

    def test_case_bin_chromosome_length_not_num(self):
        """
        Test 3
        - See if chromosome length matches input size
        :return: None
        """
        N = "Nval"
        ch = C.Chromosome(N)
        N_assert = 0
        self.assertEquals(ch.N, N_assert)

    def test_case_bin_chromosome_unique_id_check(self):
        """
        Test 4
        - See if chromosome generates unique ID
        :return: None
        """
        N=40
        ch1 = C.Chromosome(N)
        ch2 = C.Chromosome(N)
        self.assertNotEquals(ch1.ID,ch2.ID)

    def test_case_int_chromosome_range_restrict(self):
        """
        Test 5
        For an int chromosome - see if all the integer values fall into the range specified
        :return: None
        """
        range2 = [(2, 10), (2, 10), (2, 10), (5, 15), (3, 20)]
        c = C.Chromosome(N=5, type='int', name='int_pop', range_val=range2)
        result = True
        for i in range(0,c.N):
            if c.genome[i]>=c.range[i][0] and c.genome[i]<=c.range[i][1]:
                result = True
            else:
                result=False
                break
        self.assertEquals(result, True)

    def test_case_int_chromosome_range_wrong_tuple_format(self):
        """
        Test 6
        For an int chromosome - see if all the tuples in the range are in correct format
        :return: None
        """
        range2 = [(2, 10), (2, 10), (10, 2), (5, 15), (3, 20)]
        c = C.Chromosome(N=5, type='int', name='int_pop', range_val=range2)
        self.assertEquals(c.genome, None)

    def test_case_check_if_recombination_takes_place(self):
        """
        Test 7
        Test to verify if 1-point crossover takes place and genome is modified
        :return:
        """
        r = [(2, 10), (2, 10), (2, 10), (5, 15), (3, 20)]
        c1 = C.Chromosome(N=5, type='int', range_val=r)
        c2 = C.Chromosome(N=5, type='int', range_val=r)
        c1_mod,c2_mod = recombination_1_point(c1,c2)
        

if __name__ == '__main__':
    unittest.main()