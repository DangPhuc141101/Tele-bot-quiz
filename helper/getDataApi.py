import requests
import random
def getDatFormApiLink(url):
    response = requests.request("GET", url )
    listQuestion=response.json()
    return listQuestion['results'][0]

def GetQuestion( url ):
    listQuestion =getDatFormApiLink(url)
    question = listQuestion
    print(question)
    listAnswer = question['incorrect_answers']
    listAnswer.append(question['correct_answer'])
    random.shuffle(listAnswer)
    print(listAnswer, question['correct_answer'])
    return {
        'category':question['category'],
        'typeQuestion':question['difficulty'],
        'question' :question['question'],
        'correct_answer': question['correct_answer'], 
        'listAnswer' : listAnswer,
    }

#GetQuestion('https://opentdb.com/api.php?amount=1&category=9&type=multiple')


