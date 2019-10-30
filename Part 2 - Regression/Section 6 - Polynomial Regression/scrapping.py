
    
    
import requests
from bs4 import BeautifulSoup

with requests.Session() as s:

    p = s.post("https://medium.com/", data={
        "email": 'mayank.gupta.6.88@gmail.com',
        "password": "A110c@te"
    })
    print(p.text)
