# FE 595
# MidTerm Project


# Required Libraries
#Request to use GET REST API
from requests import get
from requests import head

#for NLP textblob and different package within TextBlob
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
#Pandas for operate with Dataframes
import pandas as pd


# Import flask
from flask import Flask
from flask import jsonify
from flask import request

# First function, to get the files from the web
def getfile(Input:"String list or url with the file"):
    file_head = head(Input)
    file_get  = get(Input,stream = True)
    size = file_get.headers
    ## working on doing  a validation to avoid retrieving a file too big
    #if size < 100:
    print(size)
    print(file_head.headers)
    text = file_get.text
    return(text)

## I used this function on one of the prior assigments, it gaves the top 10 descriptors, so we can keep it and
## adjusted as needed
def topdescriptions(File_name:"Name of the file with the characters"):
    # Function to identify most common descriptors
    # As input we'll include the list of characters cleaned
    with open(File_name,'r') as whole_file:
        # Reading the whole file, as TexBlob will be applied to the whole
        whole_text = whole_file.read()
        tb_text = TextBlob(whole_text)
        adj_list =[]
        # Once the TextBlob is created, a loop is performed over the list of words
        # to identify the descriptors (PoS like JJ are adjetives)
        for word,pos in tb_text.tags:
            if pos[0:2] =="JJ":
                adj_list.append(word)
        # Creating a Dataframe indicating how many times the adjetive is on the list
        count_dataframe = pd.Series(adj_list).value_counts()
        # Printing top ten
        print("The 10 most common descriptions for characters:")
        print(count_dataframe.head(n=10))




# definition of the REST API
app = Flask(__name__)


@app.route('/midterm', methods=['GET'])

def topdescriptions():
    page = request.args.get('url', default='https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M', type=str)
    a = getfile(page)
    print(a)
    #topdescriptions('cleanedlist.txt')


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
