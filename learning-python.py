# operação a nível bitwise// 

a,b = 7,2
print(a&b) #true se todas as condições estiverem corretas
print(a|b) #true se uma das condições estiverem corretas
print(a^b) #true se uma das condições estiver correta e a outra não

#Variavéis booleano(bool)
#bool = true or false

#trocar de variavéis
nome = "de Tal"
sobrenome = "Fulano"
print(nome, sobrenome)
nome,sobrenome = sobrenome,nome
print(nome,sobrenome)

#string array
s='exemplo de string'
print(s[0])
print(s[8:])
print(s[8:10])
print(s[-1])
print(s[::-1])

#operações de string

print('c '*5)
print('texto '*4)

#caracter especial 

print('c:\documentos\ numeros.txt')
print('c:\\documentos\ numeros.txt')

#unicode

S=u'Texto armazenado em Unicode'
print(S)
type(S)

#funções
print(abs(i)) #valor absoluto de i
print(chr(73)) #caracter do código ASCII
print(ord(c) #código ASCII do caracter c
print(int(s)) #converte a string em intiero 
print(srt(i)) #converte o inteiro em string