table_width = int(input('Podaj szerokość tabeli:')) #Zakładanie rozmiarów tabeli
table_height = int(input('Podaj wysokość tabeli:'))
lst = []                                            #Tworzenie listy
for i in range(0, table_height):
    element = []
    for e in range(0, table_width):
        ele = input('Podaj kolejne wartości w wierszach.')
        element.append(ele)
    lst.append(element)
print(f'Twoja lista: {lst}')
print(lst[1][2])
# def sketch(rows = table_height, columns = table_width):
#     print(columns * )
# sketch()
