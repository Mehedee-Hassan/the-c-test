
import nltk


from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer



def get_tokens():
    with open('data.txt') as stem:
        tokens  = nltk.word_tokenize(stem.read())


    return tokens



def do_stemming(filtered):
    steammed  = []

    for f in filtered:

        #steammed.append(PorterStemmer().stem(f))
        #steammed.append(LancasterStemmer().stem(f))
        steammed.append(SnowballStemmer('english').stem(f))


    return steammed




if __name__ == "__main__":
    tokens = get_tokens()

    print ("tokens = %s" %(tokens))


    stemmed_token = do_stemming(tokens)
    print("stemmed tokens = %s" %(stemmed_token))


    resutl = dict(zip(tokens,stemmed_token))

    print("{tokens:stemmed} = %s" %(resutl))

    tagged = nltk.pos_tag(tokens)
    print("tagged=%s" % (tagged))











