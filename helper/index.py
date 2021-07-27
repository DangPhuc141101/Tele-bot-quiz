import json

def readData():
    with open("C:\\Users\\Admin\\Desktop\\TEST GIY\\tele_bot_quiz\\dataBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    users = jsonObject['users']
    print(users)
    return users

def findUserById(id):
    with open("dataBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    users = jsonObject['users']
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            return i
    return -1


def createUser(id):
    users = readData()
    users.append({
        "id_tele": id,
        "totalTrue": 0,
        "totalQuestion": 0,
        "index_question": 0,
        "type_question": 9,
        "difficulty": "multiple",
        "correct_answer":"A"
    })

    with open('dataBase.json', 'w') as jsonFile:
        json.dump(users, jsonFile)
        jsonFile.close()


def getCorrectAnswerById(id):
    users = readData()
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
        return users[indexUser]['correct_answer']

def editCorrectAnswerById(id,correctAnswer ):
    users = readData()
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
         users[indexUser]['correct_answer']=correctAnswer
    
    with open('dataBase.json', 'w') as jsonFile:
        json.dump(users, jsonFile)
        jsonFile.close()

def editTypeAddDifficulty(id, type , difficulty):
     users = readData()
     indexUser = -1
    
     for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
     if(indexUser != -1):
         if(type!=''):
             users[indexUser]['type_question']=type
         if(difficulty!=''):
             users[indexUser]['difficulty']=difficulty

     with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users': users}, jsonFile)
        jsonFile.close()

def editTotalQuestion(id , answer ):
    users = readData()
    # tìm user by index
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
        if(answer):
            users[indexUser]['totalTrue'] = users[indexUser]['totalTrue']+1
  
        users[indexUser]['totalQuestion'] = users[indexUser]['totalQuestion']+1

    # ghi file lại
    with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users':users}, jsonFile)
        jsonFile.close()
