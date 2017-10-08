import chromosome, recombination, mutation, selection

def generate_population(n,size):
    try:
        population = [chromosome.Chromosome(N=n) for i in range(0,size)]
        return population
    except:
        pass



def run(n,size_of_population):
    try:
        population = generate_population(n,size_of_population)
        population = selection.random_chromosome_selection(population)
        #pop = generate_population(30, 60)
        #for p in population:
        #    p.print_chromosome()
        updated_population = []
        for i in range(0,len(population),2):
            if i==len(population)-1:
                ch = mutation.mutation_flip_bit(population[i], probability=0.7)
                updated_population.append(ch)
            else:
                print 'i is..'+str(i)
                ch1, ch2 = recombination.recombination_n_point(population[i], population[i+1])
                ch1 = mutation.mutation_flip_bit(ch1, probability=0.7)
                ch2 = mutation.mutation_flip_bit(ch1, probability=0.7)
                updated_population.append(ch1)
                updated_population.append(ch2)


        for ch in updated_population:
            ch.print_chromosome()

    except Exception as e:
        print str(e)


#pop = generate_population(30,60)
#for p in pop:
#    p.print_chromosome()

run(10,20)