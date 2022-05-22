import math #do logarytmu

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

def logarytm(podstawa, arg):
    b = arg.real
    a = podstawa.real
    if (a > 0 and a != 1) and b > 0:
        return math.log(arg.real, podstawa.real)
    else:
        print('Liczby z poza dziedziny logarytmu!')

def calc(operator, arg1, arg2):    
    current_operation = operators[operator]
    return current_operation(arg1, arg2)



operators = {'1' : add, '2' : sub,'3' : mul, '4' : div, '5' : pot, '6' : nth_root, '7' : logarytm}

if __name__ == '__main__':
    try:
        operators = {'1' : add, '2' : sub,'3' : mul, '4' : div, '5' : pot, '6' : nth_root, '7' : logarytm}
        #str_operators = {'1' : '+', '2' : '-','3' : '*', '4' : '/', '5' : '^', '6' : '^1/'}
        store = Queue()
        print('\n------------------------------\n'+
        'Witaj w poteznym kalkulatorze TS, zostaniesz poproszony o wybor dzialnia ' +
        'oraz podanie argumrtow dzialnia.\nLiczby zespolone nalezy wpisywac w formacie X+Yj!\n'+
        '------------------------------\n')
        while True:
            #Przyjmowanie danych od uzytkownika
            operator = input('Wybierz dzialanie +(1) -(2) *(3) /(4) ^(5) \u221A(6) log(7): ')
            #wyprowadzenie argumentow         
            arg1 = input('Podaj 1 arg: ')  
            arg2 = input('Podaj 2 arg: ')

            #dodanie do kolejki wyniku
            solution = calc(operator, arg1, arg2)
            if store.size_of() == 10:
                store.dequeue()
                store.enqueue(solution)
            else:
                store.enqueue(solution)

            #podanie wyniku i pytanie o czyszczenie pamieci
            print('Wynik:', end = " ")
            print(solution)
            read = input('Czy chcesz zobaczyc historie dzialan? Y/N ')
            if read == 'Y':
                clear = input('Czy chcesz wyczyscic CALA pamiec? Y/N ')
                if clear == 'Y':
                    store.operations = []
                    print('Pamiec wyczyszczona! ')
                elif clear == 'N':
                    print('Ostatniew dzialania to... ')
                    for idx, sol in enumerate(store):
                        print(f'{idx+1}.', end = " ")
                        print(sol)
                        
    except KeyboardInterrupt:
        print("Wyjscie z programu")
