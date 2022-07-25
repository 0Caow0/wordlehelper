from collections import OrderedDict
from wordlist import words # only for testing. 


class TrieNode:
	def __init__(self, key=None):
		self.key = key
		self.children = dict()
		self.freq = 0

class Trie:
	root = None
	def __init__(self):
		'''Init function'''
		self.root = self.getNode()

	def getNode(self):
		'''setting up a new node for that key'''
		return TrieNode()

	def insertWord(self, key):
		'''creating Trie data structure using all the words'''
		cur = self.root
		for i in range(5):
			if key[i] not in cur.children:
				cur.children[key[i]] = self.getNode()
			cur = cur.children[key[i]]
			cur.freq+=1

	def delete(self, cur, keys):
		'''Inner delete function that works on nodes under root'''
		if cur and cur.children:
			for i in cur.children:
				self.delete(cur.children[i], keys)
			for key in keys:
				if key in cur.children:
					cur.children.pop(key)

	def deleteNotRequiredKeys(self,keys):
		'''Main delete function that starts with root and 
			then call recursive funtion on children of root'''
		for i in self.root.children:
			self.delete(self.root.children[i], keys)
		for key in keys:
			if key in self.root.children:
				self.root.children.pop(key)

	def returnTrie(self):
		'''A test function'''
		return self.root.children

	def sorting(self, cur):
		'''Inner sorting fucntion that works on nodes under root'''
		if cur.children:
			for i in cur.children:
				self.sorting(cur.children[i])
			cur.children = OrderedDict(sorted(cur.children.items(), key=lambda x: x[1].freq,reverse=True))

	def sortChildren(self):
		'''Sorting function that sorts the words according to their frequency
			of appearance on that position'''
		for i in self.root.children:
			self.sorting(self.root.children[i])
		self.root.children = OrderedDict(sorted(self.root.children.items(), key=lambda x: x[1].freq, reverse=True))

	def deleteAtPositionInner(self, key, position, cur):
		if position:
			for i in cur.children:
				self.deleteAtPositionInner(key, position-1, cur.children[i])
		else:
			keys = []
			for i in cur.children:
				if i != key:
					keys.append(i)
			for deletion_key in keys:
				cur.children.pop(deletion_key)

	def deleteRestAtPosition(self, key, position):
		'''Delete every other node when we know there is a fixed word at a position'''
		if position:
			for i in self.root.children:
				self.deleteAtPositionInner(key, position-1, self.root.children[i])
		else:
			keys = []
			for i in self.root.children:
				if i != key:
					keys.append(i)
			for deletion_key in keys:
				self.root.children.pop(deletion_key)
	
	def returnWordsInner(self, cur, ans, word, mustContain):
		"""Returning all words in Trie (inner function for recursion)"""
		if not cur.children:
			if len(word)==5:
				flag=True
				if mustContain:
					for j in mustContain:
						if j not in word:
							flag = False
							break
				if flag:
					ans.append(word)
		else:
			for i in cur.children:
				self.returnWordsInner(cur.children[i], ans, word+i, mustContain)

	def returnAllWordsInTrie(self, mustContain):
		"""Returning all words in Trie"""
		ans = []
		for i in self.root.children:
			word=""
			self.returnWordsInner(self.root.children[i], ans, word+i, mustContain)
		return ans

	def deleteKeyAtPositionInner(self, key, position, cur):
		if position:
			for i in cur.children:
				self.deleteKeyAtPositionInner(key, position-1, cur.children[i])
		else:
			if key in cur.children:
				cur.children.pop(key)

	def deleteKeyAtPosition(self, key, position):
		'''Delete every other node when we know there is a fixed word at a position'''
		if position:
			for i in self.root.children:
				self.deleteKeyAtPositionInner(key, position-1, self.root.children[i])
		else:
			if key in self.root.children:
				self.root.children.pop(key)
