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
    #file_head = head(Input)
    file_get  = get(Input,stream = True)
    #size = file_get.headers
    ## working on doing  a validation to avoid retrieving a file too big
    #if size < 100:
    #print(size)
    #print(file_head.headers)
    text = file_get.text
    return(text)

## I used this function on one of the prior assigments, it gaves the top 10 descriptors, so we can keep it and
## adjusted as needed
def topdescriptions(File_name:"Name of the file with the characters",Top_N:"Number of Top descriptors to be retrieved"):
    # Function to identify most common descriptors
    # As input we'll include the list of characters cleaned
    tb_text = TextBlob(File_name)
    adj_list =[]
    # Once the TextBlob is created, a loop is performed over the list of words
    # to identify the descriptors (PoS like JJ are adjetives)
    for word,pos in tb_text.tags:
        if pos[0:2] =="JJ":
            adj_list.append(word)
    # Creating a Dataframe indicating how many times the adjetive is on the list
    count_dataframe = pd.Series(adj_list).value_counts()
    result_desc = count_dataframe
    return(result_desc)




# definition of the REST API
app = Flask(__name__)


@app.route('/midterm', methods=['GET'])



def main_process():
    # defaults
    address_default = 'https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M'
    input_default = 'var'
    txt_default = 'Please, provide a text to be analyzed'
    Top_default = 10
    Option_default = "Top_descriptor"

    page = request.args.get('url', default= address_default,type=str)
    type = request.args.get('type', default =input_default , type=str)
    input_txt = request.args.get('type', default =txt_default , type=str)
    Option = request.args.get('feature', default=Option_default, type=str)
    Top_N = request.args.get('Occurrences', default=Top_default, type=int)

    if type == 'url':
        input_txt = getfile(page)

    if Option == "Top_descriptor":
        a= topdescriptions(input_txt,Top_N)
        print("result", a)
        return("OK")
    else:
        return("Nothing to show")
    # we have to look on how to send back the results, converting it to xml or json



    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
