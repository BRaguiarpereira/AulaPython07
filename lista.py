'''
Sequencia no python

-listas
-tuplas
-range
-conjuntos
-dicionarios

'''

'''
Listas
conjunto ordenado e finito de dados.

-Representado por [] (conchetes).

-Cada elemento possui um indice

-Os dados em uma lista podem ser de diferentes tipos.

'''

'''
lista1=[1,2,'tomate',4.2,false]
'''

'''
lista1=[1,2,4,5,7]
for i in range(len(lista1)):
    print(lista1[2:4])
'''

    
'''
Exibir ntervalo de uma lista:
'''

'''
lista[inicial:final]

print(lista1[2:4])

lista1=[1,2,4,5,7]
[n:]
[1:]
2457

[:n] do inicio da lista ate o elemento n-1
[:3]
124
'''

'''
Inserindo elementos em uma lista.
'''

'''
append(): insere um elemento no final da lista
'''
listaA=['IPE','LPA','LM','GA','CLD']
listaA.append('APS')
print(listaA)
'''
extend():insere os elementos de uma lista dentro de outra lista(concatenaçao)
'''
lista1=['a','b','c']
lista2=[10,25,20,25]
lista1.append(lista2)
print(lista1)

a=[1,2,3,4]
b=['a','b','c','d']
c=[4.2,5.7,10.0,8.4,6]
listona=[]
listona+=a
listona+=b
listona+=c
print(listona)
print('{}lista'.format(len(listona)))

a=[1,2,3,4]
b=['a','c','d']
c=[4.2,5.7,10.0,8.4,6]
listona=[]
listona.append(a)
listona.append(b)
listona.append(c)
print(listona)
print('{}lista\n'.format(len(listona)))


print('LISTA COM FOR !!!\n')
for i in range (0,len(listona)):
    for j in range (0,len(listona[i])):
        print(listona[i][j])

'''
insert():(indice,elemento)
lista.insert
SE INDICE>LEN(lista):
-insere como ultimo elemento

lista.insert(99,x)
[0...90] sendo x o ultimo elemento
'''
listaX=[]
for i in range (0,5):
    n=input('digite  um string')
    listaX.insert(0,n)
    print(listaX)
