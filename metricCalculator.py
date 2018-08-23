import nltk
from nltk.stem.porter import PorterStemmer
from itertools import groupby
from collections import defaultdict

# This function calculates the lexical diversity of a given text
def lexical_diversity(tokens):
    return len(set(tokens))/float(len(tokens))
################################################################

#This function calculates the lexical category if given text
def lexical_category(tokens):
    tags = nltk.pos_tag(tokens)
    return tags
############################################################

# These function calculate lexical richness based on Yule’s K characteristic
def words(entry):
        return filter(lambda w: len(w)>0,
        [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])

def yule(entry):
        # yule's I measure (the inverse of yule's K measure)
        # higher number is higher diversity - richer vocabulary
        d = {}
        stemmer = PorterStemmer()
        for w in words(entry):
            w = stemmer.stem(w).lower()
            try:
                d[w] += 1
            except KeyError:
                d[w] = 1

        M1 = float(len(d))
        M2 = sum([len(list(g)) * (freq ** 2) for freq, g in groupby(sorted(d.values()))])

        try:
            return (M1 * M1) / (M2 - M1)
        except ZeroDivisionError:
            return 0
##################################################################################

# This function calculates the work count percentage
def word_count_percentage(entry, lookUpWord):
    fd= nltk.FreqDist(entry)
    return fd[lookUpWord]
####################################################

# This function calculates the TF-IDF
def tfidf(corpus, vocab):
    def termfreq(matrix, doc, term):
        try: return matrix[doc][term] / float(sum(matrix[doc].values()))
        except ZeroDivisionError: return 0
    def inversedocfreq(matrix, term):
        try:
            return float(len(matrix)) /sum([1 for i,_ in enumerate(matrix) if matrix[i][term] > 0])
        except ZeroDivisionError: return 0

    matrix = [{k:v for k,v in zip(vocab, i[1])} for i in corpus]
    tfidf = defaultdict(dict)
    for doc,_ in enumerate(matrix):
        for term in matrix[doc]:
            tf = termfreq(matrix,doc,term)
            idf = inversedocfreq(matrix, term)
            tfidf[doc][term] = tf*idf

    return [[tfidf[doc][term] for term in vocab] for doc,_ in enumerate(tfidf)]
####################################################