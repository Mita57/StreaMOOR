import psycopg2
import random
from random_word import RandomWords
import re

online = (True, False, False)
streaming = (True, False, False)
banned = (True, False, False, False)
curr_hub = ('gaming', 'creative', 'science', 'etc', 'irl', 'podcasts')
words = []

with open('asf.txt') as f:
    content = f.readlines()
for x in content:
    words.extend(re.findall(r'\b\S+\b', x))

for i in range(4999):
    local_desc = ''
    while local_desc == '' or local_desc == '\n':
        local_desc = random.choice(content)
    local_hub = random.choice(curr_hub)
    local_online = random.choice(online)
    local_email = random.choice(words) + random.choice(words) + random.choice(words) + '@gmail.com'
    local_nickname = random.choice(words) + random.choice(words)
    local_password = random.choice(words) + random.choice(words)
    local_join = str(random.randrange(2010, 2019, 1)) + '-' + str(random.randrange(1, 12, 1)) + '-' + str(random.randrange(1, 28, 1))
    local_subs = random.randrange(0, 8323234, 1)
    if(local_online):
        local_str = random.choice(streaming)
    else:
        local_str = False
    conn = psycopg2.connect(database='streamoor', user='postgres',
                     password='3395925000', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("""INSERT INTO users VALUES (%s, %s, %s, 'Null', %s,  %s, %s, %s, %s, %s, %s)""",
                (local_email, local_nickname, local_password, local_join, local_subs, local_desc, False, local_online,
                local_hub, local_str))
    conn.commit()