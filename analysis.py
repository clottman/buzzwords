from __future__ import division
import nltk
from nltk import FreqDist
from nltk import ConditionalFreqDist
from nltk.corpus import stopwords

# includes nltk code samples from http://desilinguist.org/pdf/crossroads.pdf

f = open('raikesText.csv')
raw = f.read()
tokens = nltk.word_tokenize(raw)
words = [w.lower() for w in tokens]
stopwords = set(stopwords.words("english"))
filtered_words = [w for w in words if not w in stopwords]
additionalStops = ['g', 'get', ',', ':', '(', ')', ' ', '&', "-"]
filtered_words = [w for w in filtered_words if not w in additionalStops]
fd = FreqDist()

for word in filtered_words:
	fd.inc(word)

print "Number of words: " + str(fd.N()) #total num samples
print "Number of unique words: " + str(fd.B()) #num unique samples

print "\nTop 50 Most commonly used words (by number of occurrences)"
for word in fd.keys()[:50]:
	print word, fd[word]
buzzCounter = fd['innovation'] + fd['innovative']	
print "\nAppearances of innovative or innovation: " + str(buzzCounter) + " times"
print "\nAppearances of world-class: " + str(fd['world-class'])
print "\nAppearances of Stanford: " + str(fd['stanford'])
print "\nAppearances of marriage: " + str(fd['marriage'])
print "\nAppearances of love: " + str(fd['love'])
cfd = ConditionalFreqDist()
#for each token, count the current word given previous word
prev_word = None
for word in filtered_words:
	cfd[prev_word].inc(word)
	prev_word = word
	
print "\nWords that follow innovative at least once: "
followingWords = cfd['innovative'].samples()
for follower in followingWords:
	print follower
	

