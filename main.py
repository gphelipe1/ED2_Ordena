import re
import ordena
import acentuacao
from unicodedata import normalize


'''
Por: Gabriel Phelipe
Usando Python 3

'''
#==========DICTIONARY MANIPULATION=============
def cria_dicionario(arq):
	array=[]
	dictionary={}

	with open(arq) as arquivo:
		for line in arquivo:
			linha=line.lower()
			array += re.split(r"\W+", linha)

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

def printArray(arr1,arr2):
	for i, j in zip(arr1, arr2):
		print(str(i) + ":" + str(j))
#===================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~
dic={}
a=0
metodo=1
while(a != 9):
	print("\n=========== PLAY THE PROGRAM? ===========\n")
	print("\t[Y]\n")
	print("\t[N]\n")
	play=input()
	if(play=='n'or play=='N'):
		break
	caminho=input('Digite o nome do arquivo\n')
	print("\tWAIT A FEW SECONDS :)    ...")
	dic=cria_dicionario(caminho)
	array_word=dict_to_array_word(dic)
	array_freq=dict_to_array_freq(dic)
	n=len(array_word)
	b=0
	while(b!=9):
		print("\n===========MENU ============\n")
		print("1 - Escolher Metodo")
		print("2 - Escolher tipo de ordenacao")
		print("3 - Sair")
		print("\n=============================\n")
		resp=int(input())
		if(resp==1):
			print("=============================================")
			print("\n \t 1 - Ordem alfabetica\n")
			print("\n \t 2 - Ordem decrescente de frequencia\n")
			print("=============================================")
			metodo=int(input())
		elif(resp==2):
			print("=============================================")
			print("\n \t 1 - InsertionSort")
			print("\n \t 2 - QuickSort")
			print("\n \t 3 - ShellSort")
			print("\n \t 4 - HeapSort")
			print("\n \t 5 - Binary InsertionSort")
			print("=============================================")
			sortmetod=int(input())
			if(metodo !=1 and metodo !=2):
				metodo=1
			elif(metodo==1):
				if(sortmetod==1):
					ordena.insertionSortAlfa(array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==2):
					ordena.quickSortAlfa(array_word,0,n-1)
					printArray(array_freq,array_word)
				elif(sortmetod==3):
					ordena.shellSortAlfa(array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==4):
					ordena.heapSortAlfa(array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==5):
					ordena.binary_insert_sortAlfa(array_word)
					printArray(array_freq,array_word)
			elif(metodo==2):
				if(sortmetod==1):
					ordena.insertionSortfreq(array_freq,array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==2):
					ordena.quickSortFreq(array_freq,0,n-1,array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==3):
					ordena.shellSortFreq(array_freq,array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==4):
					ordena.heapSortFreq(array_freq,array_word)
					printArray(array_freq,array_word)
				elif(sortmetod==5):
					ordena.binary_insert_sortFreq(array_freq,array_word)
					printArray(array_freq,array_word)
		elif(resp==3):
			b=9


#ordena.shellSort(array_word)
#ordena.heapSort(array_word)
#ordena.binary_insert_sort(array_word)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
