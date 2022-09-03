word_bank = {'love': {'noun': ['love', 'partner', 'se'], 
                      'verb': ['is', 'are'],
                      'adjective': ['good', 'bad', 'awesome'],
                      },
             'life': {'noun': ['life', 'success', 'money'],
                      'verb': ['is', 'are'],
                      'adjective': ['superb', 'amazing'],
                      },
             'work': {'noun': ['money', 'career', 'work'],
                      'verb': ['is', 'are'],
                      'adjective': ['fast', 'rewarding', 'engaging'],
                      },
            }

def pick_topic(d):
    print('CHOOSE A TOPIC: ')
    topics = []
    for key in d.keys():
        topics.append(key.upper())
    for index, topic in enumerate(topics):
        print(index, topic)
    
    choice = input('YOUR CHOICE: ')
    return int(choice)

def pick_noun(d):
    pass

def pick_verb(d):
    pass

def pick_adjective(d):
    pass

def make_status():
    pass