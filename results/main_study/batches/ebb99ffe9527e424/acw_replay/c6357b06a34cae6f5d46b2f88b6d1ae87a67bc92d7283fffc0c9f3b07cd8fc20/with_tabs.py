class NLPDataProcessor:
	def construct_stop_word_list(self):
		return ["a", "an", "the"]

	def remove_stop_words(self, string_list, stop_word_list):
		answer = []
		for string in string_list:
			string_split = string.split()
			for word in string_split:
				if word in stop_word_list:
					string_split.remove(word)
			answer.append(string_split)
		return answer

	def process(self, string_list):
		stop_word_list = self.construct_stop_word_list()
		return self.remove_stop_words(string_list, stop_word_list)
