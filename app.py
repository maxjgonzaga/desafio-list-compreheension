'''
MODULO 10 - PYTHONISTA AUTODIDATA  - Aula 02 - Guia completo de como usar List Compreheension

# Desafio 1
# Usando a lista compreheension, crie a seguinte lista:
[2, 4, 6, 8, 10]
'''
# RESOLUÇÃO DESAFIO 1
import random
from pprint import pprint
pprint([i*2 for i in range(1, 6)])

'''# Desafio 2
# Use a seguinte lista como base:
cores = ['vermelho','azul','verde','amarelo','rosa','preto']
# Para criar a lista a seguir:
['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rose','6 - preto']'''

# RESOLUÇÃO DESAFIO 2
# from pprint import pprint
cores = ['1 - vermelho', '2 - azul', '3 - verde',
         '4 - amarelo', '5 - rose', '6 - preto']
pprint([str(cores.index(cor)+1) + '-' + cor for cor in cores])

'''# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','marcia','cris']

Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais 
somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final deve ser 
como a lista a seguir:

['joael PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']
'''

# RESOLUÇÃO DESAFIO 3
# from pprint import pprint
participantes = ['joel', 'jessica', 'maria',
                 'cris', 'Larissa', 'rafael', 'marcus', 'john']
pagamento_realizado = ['joel', 'jessica', 'marcia', 'cris']
pprint([i + ' PAGO' if i in
        pagamento_realizado else i +
        ' DEVENDO' for i in participantes])
