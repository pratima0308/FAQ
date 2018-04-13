import re
import elasticsearch
es = elasticsearch.Elasticsearch()

txtFile = open('utd_faq.txt', 'r')
questionPattern = re.compile('Q[0-9]*. ')
answerPattern = re.compile('A[0-9]*. ')
faq = {}
count = 1
for line in txtFile:
	question = line
	answer = next(txtFile)
	modQuestion = question.split(re.findall(questionPattern, question)[0])
	modAnswer = answer.split(re.findall(answerPattern, answer)[0])
	question = modQuestion[1].split('\n')[0]
	answer = modAnswer[1].split('\n')[0]
	faq[count] = {}
	faq[count]['question'] = question
	faq[count]['answer'] = answer
	count +=1

print faq
for idx in faq.keys():
	es.index(index='corpus', doc_type='unoptimized_faq_matching', body={
		'question' : faq[idx]['question'],
		'answer' : faq[idx]['answer']
	})
