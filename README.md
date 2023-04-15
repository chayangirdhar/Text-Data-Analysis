
# Text Data Analysis 

Main objective of this project is to Use BeautifulSoup,a web scraping tool, collect text data from various text article sites and then analyse them using following parameters:

    1. POSITIVE SCORE
    2. NEGATIVE SCORE
    3. POLARITY SCORE
    4. SUBJECTIVITY SCORE
    5. AVG SENTENCE LENGTH
    6. PERCENTAGE OF COMPLEX WORDS
    7. FOG INDEX
    8. AVG NUMBER OF WORDS PER SENTENCE
    9. COMPLEX WORD COUNT
    10. WORD COUNT
    11. SYLLABLE PER WORD
    12. PERSONAL PRONOUNS
    13. AVG WORD LENGTH





## Workflow

1. Using BeautifulSoup for extracting data from any text article website, ignoring the header and footer of the site, and only extracting the text data of that article and saving it as a text file to system.

2. Using the saved text file of the article and implementing data cleaning on it by converting it to an array of words using the NLTK library, removing stop words , punctuation, etc.

3. Performing text analysis on the clean data as [Calculation References](https://github.com/chayangirdhar/Text-Data-Analysis-/edit/main/README.md#calculation-references).

4. Saving output to a saperate Text file.


## Calculation References 

1. POSITIVE SCORE = Number of words in document from [Positive words](Text-Data-Analysis/positive-words.txt) file

2. NEGATIVE SCORE = Number of words in document from [Negative words](Text-Data-Analysis/negative-words.txt) file

3. POLARITY SCORE = (Positive Score – Negative Score)/((Positive Score + Negative Score) + 0.000001)

4. SUBJECTIVITY SCORE = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)

5. AVG SENTENCE LENGTH = Number of words/Number of sentences

6. PERCENTAGE OF COMPLEX WORDS = Number of complex words/ Number of words * 100

7. FOG INDEX = 0.4 *(Average Sentence Length + Percentage of Complex words)

8. AVG NUMBER OF WORDS PER SENTENCE = Number of words/Number of sentences

9. COMPLEX WORD COUNT = Words with more than two syllabels

10. WORD COUNT = Total number of words after removing punctuations and stop words

11. SYLLABLE PER WORD = Number of vowels with "es" and "ed" as exception

12. PERSONAL PRONOUNS =  counts of the words - “I,” “we,” “my,” “ours,” and “us”

13. AVG WORD LENGTH = Total number of character / Number of Words


## Acknowledgements

 - [List of Positive and Negative words](http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar)
 - [Article Used as Example](https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

