import random

word_bank = {'love': {'noun': ['love', 'partner', 'sex'], 
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
    choice_d = {}
    for key in d.keys():
        topics.append(key.upper())
    for index, topic in enumerate(topics):
        print(index, topic)
        choice_d[index] = topic    
    choice = int(input('YOUR CHOICE: '))
    choice = choice_d[choice]
    return choice

def pick_words(d, topic):
    l = []
    keys = ()
    for key in d[topic.lower()].keys():
        keys.add(key)

    counter = 0
    while counter <= 3:
        l.append(random.choice(d[topic.lower()][keys[0]]))
        counter += 1
    print(l)

pick_words(word_bank, pick_topic(word_bank))

# print(pick_words(word_bank, pick_topic(word_bank)))  
          

def pick_verb(d):
    pass

def pick_adjective(d):
    pass

def make_status():
    pass