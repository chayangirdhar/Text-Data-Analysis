import pandas as pd
from bs4 import BeautifulSoup
import requests
import string
import nltk 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import os
import re 


def data_extration(url):
    html_text=requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    page_header = soup.title.string
    content = soup.findAll(attrs={'class':'td-post-content'})    
    content = content[0].text.strip()    
    content = content.translate(str.maketrans('', '', string.punctuation))
    file_content = page_header+ content

    with open(f'D:\classes\Work\github\output\output_content.txt','w',encoding="utf-8") as f:
        f.write(file_content)

def get_filedata(name):
    with open(f'github/output/{name}','r',encoding="utf-8") as f:
        content = f.read()
        content = content.replace('\n\n',"\n")
        content = content.replace('\n',".")
    return content


def text_analysis(content):
    pos_count=0
    neg_count=0
    sentences=0 
    total_syllables = 0
    with open('github\positive-words.txt' , 'r') as f:
        positive_words =f.read()
    with open('github\\negative-words.txt' , 'r') as f:
        negative_words =f.read()
    words = word_tokenize(content) 
    from nltk.corpus import stopwords
    nltk.download('punkt')
    nltk.download('stopwords')

    stop_words = stopwords.words('english')

    filtered_words = [word for word in words if not word in stop_words]

    ## Number of Words 
    no_words = len(filtered_words)

    ## Calculating positive score 
    for i in range(len(filtered_words)):
        if filtered_words[i] in positive_words:
            pos_count +=1

    ## Calculating negative score
    for i in range(len(filtered_words)):
        if filtered_words[i] in negative_words:
            neg_count +=1
    
    ## Calculating polarity Score
    Polarity_Score = (pos_count - neg_count)/((pos_count+neg_count)+0.000001)
    
    ## Calculating Subjectivity Score
    Subjectivity_Score = (pos_count+neg_count)/(no_words+0.000001)

    filtered_sentence = ' '.join(filtered_words)

    ## Calculating Average Sentence Length & words per sentence
    sentences += content.count('.')
    avg_sentence_len = len(words)/sentences
    avg_word_per_sentence = len(words)/sentences
    
    

    ## Calculating complex words count
    count = 0
    for word in filtered_words:
        if len(re.findall(r'[aeiouy]+', word)) > 2:
         count+=1
    Complex_words = count

    ## Calculating complex percentage
    per_complex_words = Complex_words/no_words*100

    ## Calculating FOG index
    FOG_index = 0.4 * (avg_sentence_len + per_complex_words)

    ## Calculating syllable per word 
    for word in filtered_words:
        if word.endswith("es") or word.endswith("ed"):
            continue
        total_syllables +=  len(re.findall(r'[aeiouy]+', word))
    syllable_per_words = total_syllables/no_words


    ## Calculating Personal Pronouns
    personal_pronoun = len(re.findall(r'\b(i|I|we|WE|We|my|MY|My|ours|Ours|OURS|us|Us)\b' , filtered_sentence))

    ## Calculating Avg Word Length
    total_length = sum(len(word) for word in filtered_words)
    avg_word_length = total_length/no_words

    with open(f'D:\classes\Work\github\output\\analysis_output.txt','a',encoding="utf-8") as f:

        f.write(f"POSITIVE SCORE : {pos_count} \n")
        f.write(f"NEGATIVE SCORE : {neg_count}\n")
        f.write(f"POLARITY SCORE : {Polarity_Score}\n")
        f.write(f"SUBJECTIVITY SCORE : {Subjectivity_Score}\n")
        f.write(f"AVG SENTENCE LENGTH : {avg_sentence_len}\n")
        f.write(f"PERCENTAGE OF COMPLEX WORDS : {per_complex_words}\n")
        f.write(f"FOG INDEX : {FOG_index}\n")
        f.write(f"AVG NUMBER OF WORDS PER SENTENCE : {avg_word_per_sentence}\n")
        f.write(f"COMPLEX WORD COUNT : {Complex_words}\n")
        f.write(f"WORD COUNT : {no_words}\n")
        f.write(f"SYLLABLE PER WORD : {syllable_per_words}\n")
        f.write(f"PERSONAL PRONOUNS : {personal_pronoun}\n")
        f.write(f"AVG WORD LENGTH : {avg_word_length}\n")
        f.close()

def main():
    url =  'https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/'
    data_extration(url)
    content = get_filedata("output_content.txt")
    text_analysis(content)

if __name__ == '__main__':
    main()
