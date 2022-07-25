import pickle
from triecreation import Trie
from wordlist import words
import os

def loadPickle():
	'''Retrive the tree data from pickle'''
	pickleFile = open('WordPickle', 'rb')
	return pickle.load(pickleFile)

def introMsg(n):
	if n == 0:
		print("WORDLE HELPER")
		print("How to use:-")
		print("1. Insert the word used in wordle")
		print("2. Insert a list of numbers represeting the reponse from wordle.")
	print("Insert numbers as :- ")
	print("		1 if charcter at current position is not in wordle")
	print("		2 if charcter at current position is wordle and at not this position")
	print("		3 if charcter at current position is in wordle and correct position")


def runFunction(wordTrie):
	mustContain = set()
	for _ in range(6):
		suggestions = wordTrie.returnAllWordsInTrie(mustContain)
		if len(suggestions)>1:
			introMsg(_)
		print("Top(10(?)) Suggested Words :" , *suggestions[:20])
		if len(suggestions)==1 or _ == 5:
			break
		print("enter 5 chacter word that you just used: ")
		currentGuess = input()
		print("Enter their positions as found in Wordle response seperated by space:")
		currentPositions = list(map(int, input().split()))
		for ind in range(5):
			if currentPositions[ind]==1:
				wordTrie.deleteNotRequiredKeys(currentGuess[ind])
			elif currentPositions[ind]==3:
				mustContain.add(currentGuess[ind])
				wordTrie.deleteRestAtPosition(currentGuess[ind],ind)
			else:
				mustContain.add(currentGuess[ind])
				wordTrie.deleteKeyAtPosition(currentGuess[ind],ind)
		os.system("cls")


wordTrie = loadPickle()
while True:
	runFunction(wordTrie)
	retry = input("RETRY (y/n)?")
	if retry == "y":
		wordTrie = loadPickle()
		runFunction(wordTrie)
	else:
		exit()