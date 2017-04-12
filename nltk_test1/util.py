import nltk
from collections import Counter
import string
from nltk.corpus import stopwords


def get_tokens():
    with open('data.txt') as pearl:
        tokens = nltk.word_tokenize(pearl.read().translate(string.punctuation))

    return tokens



if __name__ == "__main__":

    tokens = get_tokens()
    print("tokens=%s" %(tokens[:20]))

    countA = Counter(tokens)

    print("before :len(count) = %s" %(len(countA)))

    print("count print : %s" %(countA))

    print((stopwords.words('english')))


    filtered  = [w for w in tokens if not w in stopwords.words('english')]

    print("filtered tokens[:20] = %s" %(len(filtered[:20])))


    countB = Counter(filtered)
    print("count print : %s" %(countB))


    print("after :len(count) = %s" % (len(countB)))


    #pos tagging
    tagged = nltk.pos_tag(tokens)
    print("tagged=%s" %(tagged))



