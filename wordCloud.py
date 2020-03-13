def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    wordsList=file_contents.split()
    punc=[]
    for char in punctuations:
        punc.append(char)
    myMain=[]
    for x in wordsList:
        y=x.lower()
        if y not in uninteresting_words and y not in punc:
            myMain.append(y)
    myDic={}
    for x in myMain:
        if x not in myDic:
            myDic[x]=1
        else:
            myDic[x] +=1
    return myDic
