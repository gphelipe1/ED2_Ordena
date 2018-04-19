import re
import ordena
import acentuacao
from unicodedata import normalize


'''
Usando Python 3

'''
#==========DICTIONARY MANIPULATION=============
def cria_dicionario(arq):
	array=[]
	dictionary={}
	with open(arq) as arquivo:
		for line in arquivo:
			linha=line.lower()
			array += linha.split()

	for palavra in array:
		if len(palavra) >= 4:
			if palavra in dictionary:
				dictionary[palavra] += 1
			else:
				dictionary[palavra] = 1
	return dictionary

def dict_to_array_word(dicionario):
	array_word=[]
	array_word=list(dicionario.keys())
	return array_word


def dict_to_array_freq(dicionario):
	array_freq=[]
	for word in dicionario:
		array_freq.append(dicionario[word])
	return array_freq

#===============================================



#==============OTHERS===============

def cmp_palavras(palavra1, palavra2, tamanho_min_palavra=4):

	if(len(palavra1) >= tamanho_palavra and len(palavra2) >= tamanho_palavra):
		
		menor = len(palavra1)
		if len(palavra2) < menor:
			menor = len(palavra2)

		# Retorna 1 se "palavra1" vem primeiro que "palavra2", caso contrario, retorna zero
		
		for current_letter in range(menor):
			
			if (palavra1[current_letter] > palavra2[current_letter]):
				return 1
			elif (palavra1[current_letter] < palavra2[current_letter]):
				return 0
#===================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~
arq="entrada.txt"
dic={}
dic=cria_dicionario(arq)

array_word=dict_to_array_word(dic)
#array_freq=dict_to_array_freq(dic)
n=len(array_word)

#ordena.insertionSort(array_word)
#ordena.quickSort(array_word,0,n-1)
#ordena.shellSort(array_word)
#ordena.heapSort(array_word)
#ordena.binary_sort(array_word) --- need to be fixed

print(array_word)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
