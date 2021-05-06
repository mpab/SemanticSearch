from nltk.corpus import wordnet

syns = wordnet.synsets("program")
print(syns[0].name())
print(syns[0].definition())
print(syns[0].examples())
