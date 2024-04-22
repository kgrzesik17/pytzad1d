import operacje_na_plikach as files

def onp_test():
    files.create('plik', 'txt', 'siala baba mak ')
    files.create('plik1', 'txt', 'siala baba mak ')

    files.edit('plik.txt', 'nie wiedziala jak ', True)
    files.edit('plik1.txt', 'nie wiedziala jak ')

    print('Odczyt pierwszego pliku: ',end="")
    files.read('plik.txt', True)

    print(f'Odczyt drugiego pliku: {files.read("plik1.txt")}')

    files.delete('plik.txt', True)
    files.delete('plik1.txt')

onp_test()