import math 

repetitions = 3
max_iter = 500
mut_rate = 0.2
pop_size = 150
opseg = [-10, 10]
zaokruzivanje = 10

def levijeva_funkcija(x, y):
    return math.pow(math.sin(3*math.pi*x), 2) + math.pow(x - 1, 2)*(1 + math.pow(math.sin(3*math.pi*y), 2)) + math.pow(y - 1, 2)*(1 + math.pow(math.sin(2*math.pi*y), 2))
