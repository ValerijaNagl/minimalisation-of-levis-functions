import random
import sys
import math 
from config import \
    levijeva_funkcija, \
    max_iter, \
    mut_rate, \
    repetitions, \
    pop_size, \
    opseg, \
    zaokruzivanje
    
    


# funkcija troska je funkcija koju treba da minimizujemo
def funkcija_troska(hromozom): 
  return round(levijeva_funkcija(hromozom[0], hromozom[1]),zaokruzivanje)


#tackasta normalna mutacija
def mutacija(hromozom, rate): 
  if random.random() < rate: 
    for i in range(len(hromozom)): 
      hromozom[i] += random.gauss(0, 1) 
  return hromozom


def selekcija(populacija, velicina): 
  list = []
  # biraju se hromozomi koji ce ucestvovati u turnirskoj selekciji
  while len(list) < velicina:
      list.append(random.choice(populacija))
  najbolji = None
  najbolji_f = None
  # trazi se najbolji hromozom od izabranih pomocu funkcije troska
  for hromozom in list:
      rezultat = funkcija_troska(hromozom)
      if najbolji is None or rezultat < najbolji_f:
          najbolji_f = rezultat
          najbolji = hromozom
  return najbolji

# heuristicko ukrstanje
def ukrstanje(hrom1, hrom2): 
  novi_hromozomi = [[],[]] 
  for i in range(2): 
    for j in range(2):
    # treba nam random vrednost od 0 do 1
      random_vrednost = random.random()
      novi_hromozomi[i].append(random_vrednost*(hrom1[j] - hrom2[j]) + hrom1[j])
  return novi_hromozomi


def genetski_algoritam():

    npop_size = pop_size
    outfile = sys.stdout
    
    najbolji_rezultati = []
    prosecne_vrednosti = []
    
    print('Pokretanje genetskog algoritma.\n', file=outfile)
    for k in range(repetitions):
        best_chromosome = None
        best_fitness_value = None
        iter = 0
    
        best = []
        average = []
    
        # generisanje populacije pomocu zadatog opsega realnih vrednosti
        pop = [[random.uniform(*opseg) for i in range(2)] for j in range(pop_size)]
    
        # ponavljamo dok ne postignemo maksimum iteracija ili dok trosak ne postane 0
        while best_fitness_value != 0 and iter < max_iter:
            new = int(pop_size/2)
            new_pop = pop[:new]
    
            while len(new_pop) < npop_size:
                chrom1 = selekcija(pop, 3)
                chrom2 = selekcija(pop, 3)
                chrom3, chrom4 = ukrstanje(chrom1, chrom2)
                mutacija(chrom3, mut_rate)
                mutacija(chrom4, mut_rate)
                new_pop.append(chrom3)
                new_pop.append(chrom4)
    
            # sortiramo hromozome po trosku i ostavljamo prvu polovinu za narednu generaciju
            pop = sorted(new_pop, key=lambda chrom : funkcija_troska(chrom))[:pop_size]
            # proveravamo trosak prvog iz niza i proveravamo da li je najbolje resenje
            trosak = funkcija_troska(pop[0])
            # ako smo nasli bolji od prethodnog, azuriramo najbolje resenje
            if best_fitness_value is None or best_fitness_value > trosak:
                best_fitness_value = trosak
                best_chromosome = pop[0]

            # trosak svih clanova populacije u toj generaciji 
            prosek_generacije = round(sum(map(funkcija_troska, pop)) / pop_size, zaokruzivanje)
            # najbolju prilagodjenost je prvi hromozom iz sortirane
            average.append(prosek_generacije)
            # za svaku generaciju pamtimo najbolji trosak
            best.append(trosak)
            iter += 1
    
    
        najbolji_rezultati.append(best)
        prosecne_vrednosti.append(average)
        print("Pokretanje: ", k+1)
        print('Algoritam se zavrsio u {} generacija.'.format(iter))
        print('Najbolji hromozom : ', [round(best_chromosome[0],1), round(best_chromosome[1], 1)])
        print('\n')
    
    
  
genetski_algoritam()