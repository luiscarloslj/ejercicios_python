#lphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10, '11, '12, '13, '14, '15, '16, '17, '18, '19, '20, '21, '22, '23, '24, '25, '26, '27]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#lphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10, '11, '12, '13, '14, '15, '16, '17, '18, '19, '20, '21, '22, '23, '24, '25, '26]
for i in range(len(alphabet), 1, -1):
    print(i, "Cuanta humana, principio")
    if i % 3 == 0:
        print(i, "i despues del if, C..H..")
        print(i-1, "i despues del if Position..Python")
        alphabet.pop(i-1)
        print(i, "i despues del pop, C..H..")
        print(alphabet)



    
    