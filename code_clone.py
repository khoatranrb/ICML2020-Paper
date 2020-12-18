from bs4 import BeautifulSoup
import urllib.request
import re

def get_til(info):
    til = str(info.find('p', class_='title'))
    return til.split('>')[1].split('<')[0].replace('\xa0', ' ')

def get_aut(info):
    til = str(info.find('span', class_='authors'))
    return til.split('>')[1].split('<')[0].replace('\xa0', ' ')
def get_link(info):
    til = str(info.find('p', class_='links'))
    try:  
        return til.split('][')[1].split('"')[1], til.split('][')[2].split('"')[1]
    except:
        return til.split('][')[1].split('"')[1]

f = open('README.md', 'w+')
f.write('This repo contains ICML2020 papers. It is cloned from [this source](http://proceedings.mlr.press/v119/).')
f.write('\n')
f.write('|Title|Aut|Paper|Sup|')
f.write('\n')
f.write('|-|-|-|-|')
f.write('\n')
url =  'http://proceedings.mlr.press/v119/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(len(soup.find('body').find('main').find_all('div',class_='paper')))
for info in soup.find('body').find('main').find_all('div',class_='paper'):
    til = get_til(info)
    aut = get_aut(info)
    try:
        link, sup = get_link(info)
        f.write('|{0}|{1}|[Link]({2})|[Link]({3})|\n'.format(til, aut, link, sup))
    except:
        link = get_link(info)
        f.write('|{0}|{1}|[Link]({2})|None|\n'.format(til, aut, link))
f.write('\n')
f.close()
