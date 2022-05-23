import re
import math
import PySimpleGUI as sg
# re do dokumentacji panowie poczytajcie cos i napiszcie o tym imporcie, mozecie opisac jak dziala ten patern ponziej
# math do logarytmu o dowolnej podstawie

# potrzebny do walidacji danych liczbowych
pattern = re.compile(r'(^\d+\.?\d*[+-]\d+\.?\d*j$|^\d+\.?\d*j?$)')

class Queue(object):
    # konstruktor inicjalizuje pusta liste
    def __init__(self):
        self.operations = []

    # metoda do wpisywania na ostatnie miejsce kolejki nowa operacje
    def enqueue(self, operation):
        self.operations.insert(0, operation)

    # Metoda do usuwania pierwszej operacji
    def dequeue(self):
        return self.operations.pop()

    # zwraca dlugosc kolejki
    def size_of(self):
        return len(self.operations)

    # umozliwia iterowanie w petli po elementach kolejki
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
        window['-OUTPUT2-'].update('Nie dziel przez 0!!!')


def pot(podstawa, wykladnik):
    return podstawa ** wykladnik


def nth_root(num, n):
    return num ** (1 / n)


def logarytm(podstawa, arg):
    b = arg.real
    a = podstawa.real
    if (a > 0 and a != 1) and b > 0:
        return math.log(arg.real, podstawa.real)
    else:
        window['-OUTPUT2-'].update('Liczby z poza dziedziny logarytmu')


def calc(operator, arg1, arg2):
    current_operation = operators[operator]
    return current_operation(arg1, arg2)

######Funkcje do walidacji danych wejsciowych
def isValidDigit(text, pattern):
    while not(re.search(pattern, text)):
        window['-OUTPUT2-'].update('Bledne dane! Format to X, Yj lub X+Yj!')
        return False
    return True

def obliczenie(arg1,arg2,dzialanie):
    if isValidDigit(arg1, pattern) and isValidDigit(arg2, pattern):
        arg1 = complex(arg1)
        arg2 = complex(arg2)
        window['-OUTPUT2-'].update('')
        window['-OUTPUT-'].update('Wynik działania to:' + str(calc(dzialanie, arg1, arg2)))
        return calc(dzialanie, arg1, arg2)
    else:
        window['-OUTPUT-'].update('Brak wyniku działania!')




# Define the window's contents
layout = [[sg.Text("Wpisz pierwszy argument"), sg.Input(key='-INPUT1-')],
          [sg.Text("Wpisz drugi argument      "), sg.Input(key='-INPUT2-')],
          [sg.Button('+'), sg.Button('-'),sg.Button('*'),sg.Button('/'),sg.Button('^'),sg.Button('^1/'),sg.Button('log')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text(size=(40, 1), key='-OUTPUT2-')],
        [sg.Text(size=(40, 1), key='-OUTPUT3-')],
        [sg.Text(size=(40, 1), key='-OUTPUT4-')],
        [sg.Text(size=(40, 1), key='-OUTPUT5-')],
        [sg.Text(size=(40, 1), key='-OUTPUT6-')],
        [sg.Text(size=(40, 1), key='-OUTPUT7-')],
        [sg.Text(size=(40, 1), key='-OUTPUT8-')],
        [sg.Text(size=(40, 1), key='-OUTPUT9-')],
        [sg.Text(size=(40, 1), key='-OUTPUT10-')],
        [sg.Text(size=(40, 1), key='-OUTPUT11-')],
        [sg.Text(size=(40, 1), key='-OUTPUT12-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)
ans1, ans2,solution = None, None,None

# Display and interact with the Window using an Event Loop
while True:
    operators = {'1': add, '2': sub, '3': mul, '4': div, '5': pot, '6': nth_root, '7': logarytm}
    # str_operators = {'1' : '+', '2' : '-','3' : '*', '4' : '/', '5' : '^', '6' : '^1/'}
    store = Queue()

    event, values = window.read()
    ans1 = values['-INPUT1-']
    ans2 = values['-INPUT2-']

    if store.size_of() == 10:
        store.dequeue()
        store.enqueue(solution)
    else:
        store.enqueue(solution)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    if event == "+":
        obliczenie(ans1, ans2, '1')
    if event == "-":
        obliczenie(ans1, ans2, '2')
    if event == "*":
        obliczenie(ans1, ans2, '3')
    if event == "/":
        obliczenie(ans1, ans2, '4')
    if event == "^":
        obliczenie(ans1, ans2, '5')
    if event == "^1/":
        obliczenie(ans1, ans2, '6')
    if event == "log":
        obliczenie(ans1, ans2, '7')


# Finish up by removing from the screen
window.close()