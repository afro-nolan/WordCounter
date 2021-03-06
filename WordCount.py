#Find and counts words in a file

import sys
import string
import plotly
import plotly.graph_objs as go

def word_count(words, filename):
	count = {}
	tokens = []
	#Adds words into dictionary to be counted
	for word in words:
		count[word.strip().lower()] = 0

	#Words from file added to a list
	with open(filename) as f:
		for sentence in f:
			sentence = sentence.strip().split()
			for w in sentence:
				tokens.append(w.strip().lower())

	for word in tokens:
		word = word.strip(string.punctuation)

		#If the word is one of the given words, increment its count by one
		if word in count:
			count[word] += 1
	return count

#Will graph the results in the dictionary
def graph(count):
	words = []
	stats = []
	for key in count:
		words.append(key)
		stats.append(count[key])
	#Graph in bar chart
	data = [go.Bar(x=[w for w in words], y = [num for num in stats])]
	plotly.offline.plot(data, filename="results.html", auto_open=True)


def main():
	words = []
	sys.stdout.write("Enter words to be counted: \n")
	for word in sys.stdin:
		words.append(word)
	filename = input("Enter a filename:")
	results = word_count(words, filename)
	graph(results)



if __name__ == "__main__":
	main()

