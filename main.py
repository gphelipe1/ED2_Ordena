import re
import sort
from unicodedata import normalize


#==========DICTIONARY MANIPULATION=============
def cria_dicionario(arq):
	arquivo =open(arq, "r", -1, "ISO-8859-1") 	# => abre arquivo
	d={} 										# => cria dicionario [um HASH, nesse caso do tipo ->  ('PALAVRA', FREQUENCIA) ]
	for line in arquivo:  					  	# => pega linha por linha do arquivo
		lista=re.split(r'\W+', line) 			# => r'\W+' pega qualquer concatenacao de coisas que nao sejam palavras (digitos e letras), remove e lista as palavras
		for palavra in lista:
			if palavra in d:					# => se a palavra se encontra no dicionario
				d[palavra] +=1
			else:								# => se a palavra nao foi listada no dicionario ainda
				d[palavra] = 1
	if '' in d:
		del['']
	return d


class Dic_p_object:								# => transforma o dicionario em um objeto com palavra e frequencia
	def __init__(self, word, freq):
		self.elm = elm
		self.freq = freq

def object_p_array(obj):						# => passa os objetos criado para um array
	array=[]
	for i,j in obj.items():
		array.append(Dic_p_object(i,j))
	return array
#===============================================



#==============STR MANIPULATION===============
def remove_acentos(texto):								#funcao que remove acentos
	return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII') 

def cmp_freq(str1, str2):
    if str1.freq == str2.freq:
        return 0
    elif str1.freq < str2.freq:
        return 1
    else:
        return -1
def cmp_word(str1, str2):
	n=1
    a = remove_acentos(str1.elm)
    b = remove_acentos(str2.elm)
    for i in range(0, n):
        if i >= len(a) or i >= len(b):
            return 0
        if a[i].lower() > b[i].lower():
            return 1
        elif a[i].lower() < b[i].lower():
            return -1
    return 0
#=============================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~
a=0
while(a != 9):
		caminho=raw_input('Digite o caminho do arquivo')
	print("\n=========== MENU ============\n")

	print("\n=============================\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~