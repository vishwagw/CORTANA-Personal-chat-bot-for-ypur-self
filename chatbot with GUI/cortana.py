#'CORTANA' IS CHATBOT CREATED IN PYTHON PROGRAMMING LANGUAGE AS DEMO PROJECT.
import nltk
import warnings

warnings.filterwarnings('ignore')
import numpy as np
import nltk
import random
import string
#string library is used to proces standard python string.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('info1.txt', 'r', errors='ignore')
m = open('info2.txt', 'r', errors='ignore')
checkpoint = './chatbot_weight.ckpt'

raw = f.read()
rawone = m.read()
raw = raw.lower() #convert to lowercase
rawone = rawone.lower() #convert to lowercase
nltk.download('punkt') #for first time use
nltk.download('wordnet') #for first time
sent_tokens = nltk.sent_tokenize(raw) #to convert to list of sentences
word_tokens = nltk.word_tokenize(raw) #to convert to list of words
sent_tokensone = nltk.sent_tokenize(rawone) #to convert to list of sentences
word_tokensone = nltk.word_tokenize(rawone)#to convert to list of words

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()

#function
def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]

#for punctuations
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

#function
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#introduction for the chat bot
Introd_cort = ["My name is cortana", "i am cortana", "you can call me cortana", " my name is cortana and i am here to assist you"]

#Greeting inputs by the user
GREET_INPUT = ("hello", "hello cortana", "hi", "hey", "hey cortana", "cortana")
#response by th bot
GREET_RES = ["hello there", "Hello", "hi am here"]

#telling about the bot
about_q = ["tell me about you", "who are you", "who is this", "define your self"]
about_res = ["Hi, my name is cortana. I am an AI-powered chat bot created by Mr.Randy. i can assist you with your daily tasks annd provide you with up-to-date information."]

#thank you
thanks_in = ["Thanks", "thank you", "thank you cortana", "thank you very much"]
thanks_res = ["My pleasure mr.RANDY", "No worries", "It's a pleasure"]

#goodbye
goodbye_in = ["that's all", "good bye", "bye"]
goodbye_res = ["It was a pleasure to work with you mr.Randy. good bye and hope to see you soon..."]

#checking for greetings
def greetings(sentence):
     for word in sentence.split():
         if word.lower() in GREET_INPUT:
             return random.choice(GREET_RES)
         
#checking for introduction
def IntroduceMe(sentence):
    return random.choice(Introd_cort)

#checking about
def about(sentence):
    for word in about_q:
        if sentence.lower() == word:
            return about_res
        
#checking thank you
def thanks(sentence):
    for word in thanks_in:
        if sentence.lower() == word:
            return random.choice(thanks_res)
        
#checking goodbye
def goodBye(sentence):
    for word in goodbye_in:
        if sentence.lower() == word:
            return random.choice(goodbye_res)
        

#now we are going to generate the response by cortana:
#function1
def response(user_response):
    cort_response = ' '
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        cort_response = cort_response + "I am sorry!, I do not understand you..."
        return cort_response
    else:
        cort_response = cort_response + sent_tokens[idx]
        return cort_response

#function2
def responseone(user_response):
    cort_response = ' '
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        cort_response = cort_response + "I am sorry!, I do not understand you..."
        return cort_response
    else:
        cort_response = cort_response + sent_tokensone[idx]
        return cort_response
    
def chat(user_response):
    user_response = user_response.lower()
    flag = False
    keyword ="cortana"
    keywordone = "cortana"
    keywordsecond = "cortana"

    if (user_response != "bye"):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("CORTANA: You are welcome...")
            return "You are welcome..."
        elif (thanks(user_response) != None):
            return thanks(user_response)
        else:
            if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
                print("CORTANA: ", end="")
                print(responseone(user_response))
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif (greetings(user_response) != None):
                print("CORTANA: " + greetings(user_response))
                return greetings(user_response)
            elif (user_response.find("Your name") != -1 or user_response.find(" Your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif (about(user_response) != None):
                return about(user_response)
            else:
                print("CORTANA: ",end="")
                print(response(user_response))
                return response(user_response)
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("CORTANA: systems shutting down. good bye...")   
        return "systems shutting down. good bye..."
    
        



