import numpy as np
embedding = 50

class WordEmbedding(object):
	def __init__(self,word="",embedding=[]):
		# word must be a string, embedding can be a list or and array of ints or floats
		self.word = word
		self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
    
	def __lt__(self, other):
		# p1 < p2 calls p1.__lt__(p2)
		if isinstance(other, WordEmbedding):
			return self.word < other.word
		elif isinstance(other, str):
			return self.word < other