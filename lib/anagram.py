# your code goes here!

class Anagram:
	def __init__(self, word):
		self.word = word
		self.char_count = self.count_chars(self.word)

	def match(self, words):
		matching_words = []

		for word in words:
			curr_count = self.count_chars(word)

			if self.char_count == curr_count:
				matching_words.append(word)

		return matching_words

	def count_chars(self, word):
		char_count = [0 for _ in range(25)]

		for char in word:
			idx = ord(char) - 97
			char_count[idx] += 1

		return char_count

