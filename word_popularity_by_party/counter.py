import re
import nltk


path_dem = r"txt_files\dem4_tweets.txt"
path_rep = r"txt_files\rep_tweets.txt"
path_oth = r"txt_files\oth4_tweets.txt"

#open the file and turn the lines into one array of string tokens
def parseFile(path):
    file = open(path, "r", encoding='utf-8')
    contents = file.read() #this is of type string
    print("Read file \n")

    content_list = re.sub("[^\w]"," ", contents).split() #creating the tokens
    print("Tokenized file \n")

    tagged_tokens = nltk.pos_tag(content_list)
    print("Tagged file \n")

    return tagged_tokens

def filterbyNoun(tagged_tokens):
    nouns = []

    #I understand that this is inefficient code, but it would not run otherwise
    for token in tagged_tokens:
        if (token[1] == 'NN'):
            if(token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[0] != 's' and token[0] != 'S' and token[0] != 'U'):
                nouns.append(token[0])

        elif (token[1] == 'NNP'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                nouns.append(token[0])

        elif (token[1] == 'NNPS'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                nouns.append(token[0])

        elif (token[1] == 'NNS'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                nouns.append(token[0])

    return(nouns)


def filterbyAdjective(tagged_tokens):
    adjectives = []

    # I understand that this is inefficient code, but it would not run otherwise
    for token in tagged_tokens:
        if (token[1] == 'JJ'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                adjectives.append(token[0])

        elif (token[1] == 'JJR'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                adjectives.append(token[0])

        elif (token[1] == 'JJS'):
            if (token[0] != 'co' and token[0] != 't' and token[0] != 'https' and token[0] != 'RT' and token[
                0] != 's' and token[0] != 'S' and token[0] != 'U'):
                adjectives.append(token[0])

    return (adjectives)

#create the frequency distribution graph
def createFreqPlot(tokens_list, num_categories, title, isCumulative):
    fd = nltk.FreqDist(tokens_list)
    plot = fd.plot(num_categories, cumulative=isCumulative, title=title)
    print(plot)

#condensed
def plotbyParty(tweets_path, num_topwords, filterBy, title, isCumulative):
    # print the counts for the time series graph.
    tokens_tagged = parseFile(tweets_path)

    # filter by noun
    if(filterBy == 'noun'):
        nouns = filterbyNoun(tokens_tagged)
        print("Filtered \n")

        createFreqPlot(nouns, num_topwords, isCumulative)
        print("Plotted \n")

    if(filterBy == 'adjectives'):
        adjectives = filterbyAdjective(tokens_tagged)
        print("Filtered \n")

        createFreqPlot(adjectives, num_topwords, title, isCumulative)
        print("Plotted \n")

if __name__ == "__main__":

    #parse, calculate, and display frequency in one function
    plotbyParty(path_oth, 20, filterBy='adjectives', title="independents_adjectives", isCumulative=True)