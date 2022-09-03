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
    words = []
    keys = []
    for key in d[topic.lower()].keys():
        keys.append(key)

    counter = 0
    while counter < len(keys):
        words.append(random.choice(d[topic.lower()][keys[counter]]))
        counter += 1
    return words
          
def make_status(l):
    status = ' '.join(l)
    print('GENERATING...')
    for i in range(3):
        print(i)
    print(f'GENERATED STATUS IS: {status}')

make_status(pick_words(word_bank, pick_topic(word_bank)))