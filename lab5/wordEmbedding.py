import numpy as np
embedding = 50

class WordEmbedding(object):
	def __init__(self,word="",embedding=[]):
		# word must be a string, embedding can be a list or and array of ints or floats
		self.word = word
		self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
    
    # rich comparisons
    # https://portingguide.readthedocs.io/en/latest/comparisons.html
	def __lt__(self, other):
		if isinstance(other, WordEmbedding):
			return self.word < other.word
		elif isinstance(other, str):
			return self.word < other

	def __eq__(self, other):
		return self.word == other