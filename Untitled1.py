#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


import string


# In[3]:


import random


# In[4]:


nltk.download()


# In[5]:


nltk.download('punkt')


# In[6]:


nltk.download('wordnet')


# In[7]:


text = """Ein Chatterbot, Chatbot oder kurz Bot ist ein textbasiertes Dialogsystem, welches das Chatten mit einem technischen System erlaubt. Er hat je einen Bereich zur Textein- und -ausgabe, über die sich in natürlicher Sprache mit dem dahinterstehenden System kommunizieren lässt. Chatbots können, müssen aber nicht in Verbindung mit einem Avatar benutzt werden. Technisch sind Bots näher mit einer Volltextsuchmaschine verwandt als mit künstlicher oder gar natürlicher Intelligenz. Mit der steigenden Computerleistung können Chatbot-Systeme allerdings immer schneller auf immer umfangreichere Datenbestände zugreifen und daher auch intelligente Dialoge für den Nutzer bieten. Solche Systeme werden auch als virtuelle persönliche Assistenten bezeichnet.
Es gibt auch Chatbots, die gar nicht erst versuchen, wie ein menschlicher Chatter zu wirken (daher keine Chatterbots), sondern ähnlich wie IRC-Dienste nur auf spezielle Befehle reagieren. Sie können als Schnittstelle zu Diensten außerhalb des Chats dienen, oder auch Funktionen nur innerhalb ihres Chatraums anbieten, z. B. neu hinzugekommene Chatter mit dem Witz des Tages begrüßen.…."""


# In[8]:


text=text.lower()


# In[9]:


tokens = nltk.word_tokenize(text)


# In[10]:


lemmer = nltk.stem.WordNetLemmatizer()


# In[11]:


from nltk.corpus import stopwords


# In[12]:


def LemTokens(tokens):
   return [lemmer.lemmatize(token,'v') for token in tokens if token not in set(stopwords.words('english')) ]


# In[13]:


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


# In[14]:


def LemNormalize(text):
   return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[15]:


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# In[16]:


from sklearn.metrics.pairwise import cosine_similarity


# In[17]:


from sklearn.feature_extraction.text import CountVectorizer


# In[18]:


def response(user_response):
        sentences.append(user_response)
        cv = CountVectorizer(max_features = 50, tokenizer = LemNormalize, analyzer = 'word')
        X = cv.fit_transform(sentences)
        vals_cv = cosine_similarity(X[-1], X)
        indx_of_most_similar_sentence = vals_cv.argsort()[0][-2] 
        flat_vals_cv = vals_cv.flatten()
        flat_vals_cv.sort()
        highest_similarity = flat_vals_cv[-2]

        if(highest_similarity == 0):
              robo_response = "I am sorry! I don't understand you"
              return robo_response
        else:
              robo_response = sentences[indx_of_most_similar_sentence]
              return robo_response


# In[19]:


exit_codes = ['bye', 'see you', 'c ya', 'exit']
flag=True
print("Hi! Im a Chatty, I will try to answer your queries !")


# In[ ]:


flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")


# In[ ]:





# In[ ]:




