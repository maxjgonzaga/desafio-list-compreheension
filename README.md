# desafio-list-compreheension
Desafio List Compreeheension  - Curso Pythonista Autodidata  - Dev Aprender - Jhonatan de Souza

List Comprehensions são uma forma concisa e poderosa de criar listas em Python. Elas permitem que você crie uma lista com base em outra lista, iterando sobre seus elementos e aplicando uma expressão a cada um deles.

A sintaxe básica de uma List Comprehension é a seguinte:

nova_lista = [expressao for elemento in lista_original]

Aqui, **`expressao`** é uma expressão que será aplicada a cada **`elemento`** da **`lista_original`**, e o resultado será armazenado na **`nova_lista`**.

Por exemplo, se você tiver uma lista de números e quiser criar uma nova lista contendo o quadrado de cada número, você pode fazer isso com uma List Comprehension:

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]

qui, numero ** 2 é a expressão que eleva cada número ao quadrado, e a nova_lista quadrados conterá os quadrados de todos os números em numeros.

Você também pode adicionar uma condição para filtrar os elementos da lista original. Por exemplo, se você quiser criar uma nova lista contendo apenas os números pares da lista original, você pode fazer isso com uma List Comprehension:

numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]

Aqui, **`numero % 2 == 0`** é a condição que filtra os números pares, e a **`nova_lista`** **`pares`** conterá apenas os números pares da **`lista_original`** **`numeros`**.

As List Comprehensions são uma ferramenta poderosa e versátil em Python, e são frequentemente usadas para criar listas de forma concisa e eficiente. Elas são uma parte essencial do kit de ferramentas de qualquer programador Python.

# DESAFIO PYTHONISTA AUTODIDATA 

# Desafio 1
# Usando a lista compreheension, crie a seguinte lista:
[2, 4, 6, 8, 10]

# Desafio 2
# Use a seguinte lista como base:
cores = ['vermelho','azul','verde','amarelo','rosa','preto']

# Para criar a lista a seguir:
['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rose','6 - preto']

# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','marcia','cris']
'''
Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final deve ser como a lista a seguir:
'''
['joael PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']