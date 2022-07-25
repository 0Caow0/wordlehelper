import pickle
from wordlist import words
from triecreation import Trie


wordTrie = Trie()
for word in words:
	wordTrie.insertWord(word)
wordTrie.sortChildren()

# Moving all the Trie data structure to a new pickle file for later use
wordPickle = open('WordPickle', 'ab')
pickle.dump(wordTrie, wordPickle)
wordPickle.close()

# testing and reading
# dbfile = open('WordPickle', 'rb')
# db = pickle.load(dbfile)
# print(db.returnALlWordsInTrie())    