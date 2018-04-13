## All these scripts have been developed on Windows 10 OS and python version 2.7. 

PIP freeze for the project:
assertpy==0.13
colorama==0.3.9
elasticsearch==6.2.0
termcolor==1.1.0
-- Please add all the dependencies in python so that all python scripts work smoothly.

Elasticsearch version and setup:
1. I have installed Elasticsearch version "5.5.3". Please install the same version, as version mismatch can lead to query failure or unexpected behaviour.
2. Make an index called "corpus" in elastic search. Steps to create an index in elastic search:
-- Make a PUT request to elasticsearch with following mapping in the body.
PUT /corpus/ 
{
  "mappings": {
    "unoptimized_faq_matching": { 
      "properties": { 
        "question": { 
            "type": "text",
            "analyzer": "english" 
        }, 
        "answer": { 
            "type": "text",
            "analyzer": "english"  
        }     
      }
    }
  }
}
-- In case you have only one node of elasticsearch installed and your clusters are in unassigned state, please make the replication factor 0 using following request.
PUT /corpus/_settings
{
    "index": {
        "number_of_replicas":0
    }
}
3. Add data to elasticsearch (in oder to add data make sure your elastic search is up and running).
-- python putData.py

Corpus being used in FAQ Project
--A file named utd_faq.txt contains our entire corpus.

List of questions in FAQ Project
--A file named questions_corpus.txt contains list of all the questions.

Script to validate bag-of-words approach:

1. Run "python validate_bagOfWords_approach.py" to run test cases.
2. The script does the following things.
--It reads, one by one, all the questions from our original FAQ corpus.
--For each question, it queries our system for the best match 'FAQ' and returns the question(original) with the closest match.
--It reverses the string of the original query question, queries our system and returns the question(original) with the closest match.
--An assertion comparision is done between the query and the original question, to see if correct FAQ is returned.

Script to query our system and return top 10 best matches:    