import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.pfrwvbn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('http://localhost:63342/frontend_prac/simple_fanpage.html?_ijt=bpg7ce1tdregud0fjlqoj3fsuv',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
#card-box > blockquote:nth-child(1) > p
#card-box > blockquote:nth-child(2) > p

#card-box > blockquote:nth-child(1) > footer
comments = soup.select('#card-box')
print('1')
for comment in comments:
    word = comment.select_one('p').text
    who = comment.select_one('footer').text

    print(word)

# db.fanpageComments.insert_one(doc)
