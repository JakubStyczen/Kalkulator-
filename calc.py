#kolejka potrzebna do przechowywania ostatnich 10 dzialan
class Queue(object):
    #konstruktor inicjalizuje pusta liste
    def __init__(self):
        self.operations = []

    #metoda do wpisywania na ostatnie miejsce kolejki nowa operacje
    def enqueue(self, operation):
        self.operations.insert(0, operation)
    
    #Metoda do usuwania pierwszej operacji 
    def dequeue(self):
        return self.operations.pop()

    #zwraca dlugosc kolejki
    def size_of(self):
        return len(self.operations)

    #umozliwia iterowanie w petli po elementach kolejki
    def __iter__(self):
        return iter(self.operations)


#####FUNCKJE OBLICZAJACE
def add(arg1, arg2):
    return arg1 + arg2

def sub(arg1, arg2):
    return arg1 - arg2

def mul(arg1, arg2):
    return arg1 * arg2

def div(arg1, arg2):
    if arg2 != 0:
        return arg1 / arg2
    else: 
        print("Nie dziel przez 0!!!")  

def pot(podstawa, wykladnik):
    return podstawa**wykladnik

def nth_root(num ,n):
    return num**(1/n)