from bs4 import BeautifulSoup
import requests 
import time

#while(True):
file1 = open('menu.txt', 'w')
file2 = open('menu.txt', 'w')

#get data
data = requests.get('https://www.peddie.org/our-community/peddie-am-20')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

menu = soup.find('div', {'class':'fsListItems'})
menu2 = soup.find('div', {'class':'fsDescription'}).get_text("\n")

#print(menu2 + '\n')
file1.write(menu2)
file2.write(menu2)
file1.close()
file2.close()

#debugging:
print(__file__)