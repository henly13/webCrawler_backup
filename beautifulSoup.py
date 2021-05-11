from selenium import webdriver
from bs4 import BeautifulSoup

def happy_shopping(key:str)->list:
  ls=[]
  tags = soup.select(key)
  for i in tags:
    ls.append(i.text)
  return ls

def duplicate_check(data:list)->list:
  for i in range(len(data)-1):
    if(data[i]==data[i+1]):
        data[i]=""
                
  while "" in data:
    data.remove("")
  return data

driver = webdriver.PhantomJS(executable_path=r"C:\Users\Henly\Desktop\爬蟲\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get('https://www.happy-shopping.tw/second_class.php?fcid=2')
data = driver.page_source
driver.quit()
soup = BeautifulSoup(data, 'html.parser')
tags = soup.select('a.prod_name p')
name = happy_shopping('a.prod_name p')
price = happy_shopping('span.price')
discount = happy_shopping('span.discount')
data=[]
for i in range(len(name)):
  data.append([name[i],price[i],discount[i]])

data.sort()
data = duplicate_check(data)


for i in range(len(data)):
  print(data[i])
