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

#datetime to request system time to provide information on errors
import datetime


# Import flask
from flask import Flask
from flask import jsonify
from flask import request


# Global variables to be use between funcitons
Options_list = ('translate','identify','Top','Sentiment')
Gib_factor = 0.1
max_txt = 1000
input_default = 'var'
# the dictionary will contain the description fo ISO 639-1 language code
language_desc = dict([('ab', 'Abkhaz'),
('aa', 'Afar'),
('af', 'Afrikaans'),
('ak', 'Akan'),
('sq', 'Albanian'),
('am', 'Amharic'),
('ar', 'Arabic'),
('an', 'Aragonese'),
('hy', 'Armenian'),
('as', 'Assamese'),
('av', 'Avaric'),
('ae', 'Avestan'),
('ay', 'Aymara'),
('az', 'Azerbaijani'),
('bm', 'Bambara'),
('ba', 'Bashkir'),
('eu', 'Basque'),
('be', 'Belarusian'),
('bn', 'Bengali'),
('bh', 'Bihari'),
('bi', 'Bislama'),
('bs', 'Bosnian'),
('br', 'Breton'),
('bg', 'Bulgarian'),
('my', 'Burmese'),
('ca', 'Catalan; Valencian'),
('ch', 'Chamorro'),
('ce', 'Chechen'),
('ny', 'Chichewa; Chewa; Nyanja'),
('zh', 'Chinese'),
('cv', 'Chuvash'),
('kw', 'Cornish'),
('co', 'Corsican'),
('cr', 'Cree'),
('hr', 'Croatian'),
('cs', 'Czech'),
('da', 'Danish'),
('dv', 'Divehi; Maldivian;'),
('nl', 'Dutch'),
('dz', 'Dzongkha'),
('en', 'English'),
('eo', 'Esperanto'),
('et', 'Estonian'),
('ee', 'Ewe'),
('fo', 'Faroese'),
('fj', 'Fijian'),
('fi', 'Finnish'),
('fr', 'French'),
('ff', 'Fula'),
('gl', 'Galician'),
('ka', 'Georgian'),
('de', 'German'),
('el', 'Greek, Modern'),
('gn', 'Guaraní'),
('gu', 'Gujarati'),
('ht', 'Haitian'),
('ha', 'Hausa'),
('he', 'Hebrew (modern)'),
('hz', 'Herero'),
('hi', 'Hindi'),
('ho', 'Hiri Motu'),
('hu', 'Hungarian'),
('ia', 'Interlingua'),
('id', 'Indonesian'),
('ie', 'Interlingue'),
('ga', 'Irish'),
('ig', 'Igbo'),
('ik', 'Inupiaq'),
('io', 'Ido'),
('is', 'Icelandic'),
('it', 'Italian'),
('iu', 'Inuktitut'),
('ja', 'Japanese'),
('jv', 'Javanese'),
('kl', 'Kalaallisut'),
('kn', 'Kannada'),
('kr', 'Kanuri'),
('ks', 'Kashmiri'),
('kk', 'Kazakh'),
('km', 'Khmer'),
('ki', 'Kikuyu, Gikuyu'),
('rw', 'Kinyarwanda'),
('ky', 'Kirghiz, Kyrgyz'),
('kv', 'Komi'),
('kg', 'Kongo'),
('ko', 'Korean'),
('ku', 'Kurdish'),
('kj', 'Kwanyama, Kuanyama'),
('la', 'Latin'),
('lb', 'Luxembourgish'),
('lg', 'Luganda'),
('li', 'Limburgish'),
('ln', 'Lingala'),
('lo', 'Lao'),
('lt', 'Lithuanian'),
('lu', 'Luba-Katanga'),
('lv', 'Latvian'),
('gv', 'Manx'),
('mk', 'Macedonian'),
('mg', 'Malagasy'),
('ms', 'Malay'),
('ml', 'Malayalam'),
('mt', 'Maltese'),
('mi', 'Māori'),
('mr', 'Marathi (Marāṭhī)'),
('mh', 'Marshallese'),
('mn', 'Mongolian'),
('na', 'Nauru'),
('nv', 'Navajo, Navaho'),
('nb', 'Norwegian Bokmål'),
('nd', 'North Ndebele'),
('ne', 'Nepali'),
('ng', 'Ndonga'),
('nn', 'Norwegian Nynorsk'),
('no', 'Norwegian'),
('ii', 'Nuosu'),
('nr', 'South Ndebele'),
('oc', 'Occitan'),
('oj', 'Ojibwe, Ojibwa'),
('cu', 'Old Church Slavonic'),
('om', 'Oromo'),
('or', 'Oriya'),
('os', 'Ossetian, Ossetic'),
('pa', 'Panjabi, Punjabi'),
('pi', 'Pāli'),
('fa', 'Persian'),
('pl', 'Polish'),
('ps', 'Pashto, Pushto'),
('pt', 'Portuguese'),
('qu', 'Quechua'),
('rm', 'Romansh'),
('rn', 'Kirundi'),
('ro', 'Romanian, Moldavan'),
('ru', 'Russian'),
('sa', 'Sanskrit (Saṁskṛta)'),
('sc', 'Sardinian'),
('sd', 'Sindhi'),
('se', 'Northern Sami'),
('sm', 'Samoan'),
('sg', 'Sango'),
('sr', 'Serbian'),
('gd', 'Scottish Gaelic'),
('sn', 'Shona'),
('si', 'Sinhala, Sinhalese'),
('sk', 'Slovak'),
('sl', 'Slovene'),
('so', 'Somali'),
('st', 'Southern Sotho'),
('es', 'Spanish; Castilian'),
('su', 'Sundanese'),
('sw', 'Swahili'),
('ss', 'Swati'),
('sv', 'Swedish'),
('ta', 'Tamil'),
('te', 'Telugu'),
('tg', 'Tajik'),
('th', 'Thai'),
('ti', 'Tigrinya'),
('bo', 'Tibetan'),
('tk', 'Turkmen'),
('tl', 'Tagalog'),
('tn', 'Tswana'),
('to', 'Tonga'),
('tr', 'Turkish'),
('ts', 'Tsonga'),
('tt', 'Tatar'),
('tw', 'Twi'),
('ty', 'Tahitian'),
('ug', 'Uighur, Uyghur'),
('uk', 'Ukrainian'),
('ur', 'Urdu'),
('uz', 'Uzbek'),
('ve', 'Venda'),
('vi', 'Vietnamese'),
('vo', 'Volapük'),
('wa', 'Walloon'),
('cy', 'Welsh'),
('wo', 'Wolof'),
('fy', 'Western Frisian'),
('xh', 'Xhosa'),
('yi', 'Yiddish'),
('yo', 'Yoruba'),
('za', 'Zhuang, Chuang'),
('zu', 'Zulu')])


###
### CROSS FUNCTIONS to be used for all the options
###

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


def validations(txt_input:"Text to be validated",Option:"Option to be applied"):
    global Gib_factor
    global max_txt
    global Options_list
    if Option not in Options_list:
        return("NO OK","Option not valid")
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
        elif lng_txt == 'fy':
            return ("NO OK", "Language not supperted/not possible to identify")
        elif lng_txt != "en" and Option != "translate" and Option != "identify":
            return ("NO OK","For other languages only options are translate/identify language")

    return("OK","")


# Error function to print the possible information that it would help to fix errors    
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


###
### FEATURES to provide capabilities on the APIs
###

# Function to identify descriptors and cuantify their appearance on the input file
def topdescriptions(File_name:"Name of the file with the characters"):
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
    return("OK","",count_df)


# Identify Language function
def identify_language(txt_input:"text to identify language"):

    global language_desc

    tb_text = TextBlob(txt_input)
    lng_txt = tb_text.detect_language()

    if lng_txt in language_desc:
        lng_desc = language_desc[lng_txt]
    else:
        lng_desc = lng_txt

    return("OK","","The language of the input is "+lng_desc)

# definition of the REST API
app = Flask(__name__)

##################################################################################
##################################################################################
##################      END POINTS      ##########################################
##################      END POINTS      ##########################################
##################      END POINTS      ##########################################
##################################################################################
##################################################################################


##################################################################################
#### Main End Point in the case that the user prefer to target only one
##################################################################################
@app.route('/midterm', methods=['GET'])

def main_process():
    global input_default
    address_default = 'https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M'
    txt_default = ''
    Option_default = "Top"

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

    if Option == "Top":
        result,error,desciption_result = topdescriptions(input_txt)
        result_return = desciption_result.to_json(orient='split')
    elif Option == "identify":
        result,error,result_return = identify_language(input_txt)
    else:
        return("Nothing to show")
    if result =="OK":
        print("result", result_return)
        return ("OK", result_return)
    else:
        return ("NO OK",error)


##################################################################################
#### Descriptors End Point
##################################################################################
    
@app.route('/top', methods=['GET'])

def Top_process():
    
    global input_default
    
    page = request.args.get('url', default= "",type=str)
    type_input = request.args.get('type', default =input_default , type=str)
    input_txt = request.args.get('text', default ="" , type=str)
    
    if type == 'url':
        input_txt = getfile(page)
        
    result,error = validations(input_txt,Option)

    if result != "OK":
        print_error(Option,input_txt,type_input,page,error)
        return error

    result,error,desciption_result = topdescriptions(input_txt)
    result_return = desciption_result.to_json(orient='split')
    if result =="OK":
        return ("OK", result_return)
    else:
        return ("NO OK",error)

##################################################################################
#### Identify End Point
##################################################################################
    
@app.route('/top', methods=['GET'])

def Identify_process():
    
    global input_default
    
    page = request.args.get('url', default= "",type=str)
    type_input = request.args.get('type', default =input_default , type=str)
    input_txt = request.args.get('text', default ="" , type=str)
    
    if type == 'url':
        input_txt = getfile(page)
        
    result,error = validations(input_txt,Option)

    if result != "OK":
        print_error(Option,input_txt,type_input,page,error)
        return error

    result,error,result_return = identify_language(input_txt)
    
    if result =="OK":
        return ("OK", result_return)
    else:
        return ("NO OK",error)






    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
