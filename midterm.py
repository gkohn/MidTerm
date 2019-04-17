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
from textblob.wordnet import VERB


#Pandas for operate with Dataframes
import pandas as pd
import datetime


# Import flask
from flask import Flask
from flask import jsonify
from flask import request

# Global variables
Gib_factor = 0.1
max_txt = 1000


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
def topdescriptions(File_name:"Name of the file with the characters"):
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
    adj_list_df = pd.DataFrame({'Descriptor':adj_list})
    count_desc = adj_list_df['Descriptor'].value_counts()
    count_df = count_desc.rename_axis('Descriptor').reset_index(name='Occurences')
    print(count_df)
    return(count_df)


def identify_language(txt_input:"text to identify language"):
    tb_text = TextBlob(txt_input)
    lng_txt = tb_text.detect_language()
    print(lng_txt)

    return("OK","")

def validations(txt_input:"Text to be validated",Option:"Option to be applied"):
    global Gib_factor
    global max_txt
    if len(txt_input) > max_txt:
        return("NO OK","Text too big. The total number of admited characters is "+str(max_txt))
    if txt_input =="":
        return("NO OK","Input empty")
    else:
        tb_text = TextBlob(txt_input)
        lng_txt = tb_text.detect_language()
        print(lng_txt)
        if lng_txt == 'en':
            err_word = 0
            print(len(tb_text.tags))
            for word, pos in tb_text.tags:
                print(word,pos)
                ret_word = word.synsets
                if ret_word ==[]:
                    err_word = err_word +1
                else:
                    print(ret_word)
            if err_word/len(tb_text.tags)>Gib_factor:
                return ("NO OK","Posible Gibberish")
        elif lng_txt != "en" and Option != "translate" and Option != "identify":
            return ("NO OK","For other languages only options are translate/identify language")
        elif lng_txt == 'und':
            return ("NO OK", "Language not supperted/not possible to identify")
    return("OK","")


    
def print_error(Option,input_txt,type_input,page,error):
    currentDT = datetime.datetime.now()
    print("********************************************************ERROR********************************************************")
    print("********************************************************ERROR********************************************************")
    print("**  Error found while processing file, at:",currentDT)
    print("**  The error found was:",error)
    print("**  The first 10 characters of the text is",input_txt[1:10])
    print("**  The option used:",Option)
    print("**  The URL provided:",page)
    print("********************************************************ERROR********************************************************")
    print("********************************************************ERROR********************************************************")
    return(None)

# definition of the REST API
app = Flask(__name__)


@app.route('/midterm', methods=['GET'])



def main_process():
    
    # defaults
    address_default = 'https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M'
    input_default = 'var'
    txt_default = ''
    Option_default = "Top_descriptor"

    page = request.args.get('url', default= address_default,type=str)
    type_input = request.args.get('type', default =input_default , type=str)
    input_txt = request.args.get('text', default =txt_default , type=str)
    Option = request.args.get('feature', default=Option_default, type=str)
    

    if type == 'url':
        input_txt = getfile(page)
        
    result,error = validations(input_txt,Option)

    if result != "OK":
        print_error(Option,input_txt,type_input,page,error)
        return error

    if Option == "Top_descriptor":
        desciption_result = topdescriptions(input_txt)
        result_json = desciption_result.to_json(orient='split')
        print("result", result_json)
        return("OK", result_json)
    else:
        return("Nothing to show")
    #Results to be sent back in json



    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
