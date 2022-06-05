import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

X ="I am good"
Y ="I am well"


X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

sw = stopwords.words('english')

l1 =[]
l2 =[]

# remove stop words from the string
X_set = {w for w in X_list if not w in sw}
print(X_set)

Y_set = {w for w in Y_list if not w in sw}
print(Y_set)

rvector = X_set.union(Y_set)
print(rvector)

for w in rvector:

    # create a vector from texts
    synonyms = []

    for syn in wordnet.synsets(w):
	    for l in syn.lemmas():
		    synonyms.append(l.name())

    print(w)
    print(synonyms)

    for s in range(len(synonyms)):
        if synonyms[s] in X_set:
            l1.append(1)
            break
        else:
            if s+1 == len(synonyms):
                l1.append(0)

    for s in range(len(synonyms)):
        if synonyms[s] in Y_set:
            l2.append(1)
            break
        else:
            if s+1 == len(synonyms):
                l2.append(0)

print(l1)
print(l2)
c=0

for i in range(len(rvector)):
        c+= l1[i]*l2[i]

cosine = c / float((sum(l1)*sum(l2))**0.5)

print("similarity: ", cosine)
