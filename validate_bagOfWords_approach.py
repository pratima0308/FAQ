import elasticsearch
import re
from termcolor import colored
import colorama
import sys
colorama.init()
from assertpy import *
es = elasticsearch.Elasticsearch()

count = 1
questionPattern = re.compile('Q[0-9]*. ')
body = {
  "query": {
    "multi_match" : {
      "query": '', 
      "fields": [ "answer", "question" ] 
    }
  }
}
Introd =  [
  'Bag of words approch : Test Script',
  'Objective of this Script is to do blackbox testing of our bag-of-words approach.',
  'The script with simply query the system with all the question and reverse of question strings.'
  'The Objective is to get the exact match with the stored faqs.'
]
for line in Introd :
  text = colored(line, 'red')
  print text
questionCorpus = open('questions_corpus.txt', 'r')
questionResp = []
questionResp.append({
  'question' : '',
  'response' : '',
})
questionResp.append({
  'question': '',
  'response': '' 
})
for question in questionCorpus:
  modQuestion = question.split(re.findall(questionPattern, question)[0])[1].split('\n')[0]
  body['query']['multi_match']['query'] = modQuestion
  questionResp[0]['question'] = modQuestion
  res = es.search(index="corpus", body=body)
  questionResp[0]['response'] = res['hits']['hits'][0]["_source"]['question']
  bagOfWords = modQuestion.split(' ')
  reverseQues = ''
  for idx, word in enumerate(bagOfWords):
    if idx != 0 :
      reverseQues =  word + ' ' + reverseQues
    else:
      reverseQues = word
  body['query']['multi_match']['query'] = reverseQues
  questionResp[1]['question'] = reverseQues
  res = es.search(index="corpus", body=body)
  questionResp[1]['response'] =  res['hits']['hits'][0]["_source"]['question']
  for ele in questionResp:
    txt = colored(ele['question'], 'green')
    print 'Question : ' + txt
    txt = colored(ele['response'], 'yellow')
    print 'Response : ' + txt
  try:
    assert_that(questionResp[0]['question']).is_equal_to(questionResp[0]['response'])
    assert_that(questionResp[0]['question']).is_equal_to(questionResp[1]['response'])
    txt = colored('Test Case : ' + str(count), 'white')
    print txt
    txt = colored('Test case passed.', 'white')
    print txt
  except:
    print("Oops!",sys.exc_info()[0],"occured.")
    txt = colored('Test Case : ' + str(count), 'red')
    print txt
    txt = colored('Test case failed.', 'red')
    print txt
  count = count + 1
  
  

    