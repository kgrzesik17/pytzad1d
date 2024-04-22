import operacje_na_plikach as files
import generatory_liczb as numbers

def onp_test():
    files.create('plik', 'txt', 'siala baba mak ')
    files.create('plik1', 'txt', 'siala baba mak ')

    files.edit('plik.txt', 'nie wiedziala jak ', True)
    files.edit('plik1.txt', 'nie wiedziala jak ')

    print('Odczyt pierwszego pliku: ', end="")
    files.read('plik.txt', True)

    print(f'Odczyt drugiego pliku: {files.read("plik1.txt")}')

    files.delete('plik.txt', True)
    files.delete('plik1.txt')


def gl_test():
    print(f'The first 10 fibonacci numbers are: {numbers.fibonacci(10)}')
    print(f'The first 10 prime numbers are: {numbers.prime(10)}')
    print(f'The first 4 perfect numbers are: {numbers.perfect(4)}')
    numbers.perfect(5)

gl_test()