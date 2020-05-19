from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as ur
import requests
import json
import pycountry
from datetime import datetime
from datetime import timedelta
import re

today = datetime.today().strftime('%Y-%m-%d')
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)

URL='https://www.worldometers.info/coronavirus/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page=requests.get(URL,headers=headers)
soup=bs(page.content,'html.parser')
table_body=soup.find('table', {"id":"main_table_countries_today"})
# source_list=soup.find('div', {"id":"newsdate"+today})

table_body_yesterday=soup.find('table', {"id":"main_table_countries_yesterday"})
rows = table_body.find_all('tr')
rows_yesterday = table_body_yesterday.find_all('tr')
l=[]
d={
    "Corona":[]
}
y={
    "Corona":[]
}
s ={
    "Corona":[]
}
sy ={
    "Corona":[]
}
f={
    "Main":[]
}
#to find the Main Header
ss=[]
mains=soup.findAll("div", {"id": "maincounter-wrap"} )


for i in mains:
    ss.append(i.find("span").text)
temp=soup.find_all("div",{"class":"panel_flip"})
data1=[]
data2=[]
for k in temp:
   x=k.findAll("div",{"class":"number-table-main"})
   for i in x:
     data1.append(i.text.strip())
   m=k.findAll("span")
   for j in m:
     data2.append(j.text.strip())

 
#print(temp1)
cuinf,cloc=data1
mild,seri,dis,dea=data2
coc,cocd,rec=ss
f["Main"].append({
    "CoronaCases":coc,
    "CoronaCurrent":cuinf,
    "CoronaClose":cloc,
    "CoronaMild":mild,
    "CoronaCritical":seri,
    "CoronaDischarged":dis,
    "CoronaDeaths":dea,
    "CoronaDeaths":cocd,
    "Recoverd":rec
})

#To get table data

#To get table data
def data_today():
    mapping = {country.name: country.alpha_2 for country in pycountry.countries}
    for row in rows:
        cols=row.find_all('td')
        z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]

        #print(z)
        if len(z)!=0:
            #c,totc,newc,totd,newd,totrecv,Actcases,seri,avg,Avgd,totes,avgtes=z
            c = z[1]
            totc =z[2]
            newc =z[3]
            totd =z[4]
            newd =z[5]
            totrecv =z[6]
            Actcases=z[7]
            seri=z[8]
            avg =z[9]
            Avgd=z[2]
            totes =z[11]

            d['Corona'].append({
                "Country":c,
                "Code":str(mapping.get(c)).lower(),
                "TotalCases":totc,

                "NewCases":newc,
                "TotalDeaths":totd,
                "NewDeaths":newd,
                "TotalRecoverd":totrecv,
                "ActiveCases":Actcases,
                "Serious":seri,
                "Average":avg,
                "AverageDeaths":Avgd

            })
    return d
    
def data_yesterday():
    mapping = {country.name: country.alpha_2 for country in pycountry.countries}    
    for row in rows_yesterday:
        cols=row.find_all('td')
        z=['0' if v.text.strip() == "" else v.text.strip() for v in cols]

        #print(z)
        if len(z)!=0:
            #c,totc,newc,totd,newd,totrecv,Actcases,seri,avg,Avgd,totes,avgtes=z
            c = z[1]
            totc =z[2]
            newc =z[3]
            totd =z[4]
            newd =z[5]
            totrecv =z[6]
            Actcases=z[7]
            seri=z[8]
            avg =z[9]
            Avgd=z[2]
            totes =z[11]

            y['Corona'].append({
                "Country":c,
                "Code":str(mapping.get(c)).lower(),
                "TotalCases":totc,

                "NewCases":newc,
                "TotalDeaths":totd,
                "NewDeaths":newd,
                "TotalRecoverd":totrecv,
                "ActiveCases":Actcases,
                "Serious":seri,
                "Average":avg,
                "AverageDeaths":Avgd
            })
    return y
         
def source_today():
    
    source_list=soup.find('div', {"id":"newsdate"+today})
    # # source_list=soup.find('div', {"id":"news_block"})
    source_news_li = source_list.find_all("li", {"class":"news_li"})

    for row in source_news_li:
        url = ""
        death = ""
        case = ""
        country = ""
        for link in row.find_all('a', attrs={'href': re.compile("^http")}):
            url = link.get('href')
        strong=row.find_all('strong')
        z=['0' if v.text.strip() == "" else v.text.strip() for v in strong]
        for string in z:
            if ("case" in string): 
                case = string
            elif ("death" in string): 
                death = string
            else:
                country = string

        s['Corona'].append({
                "case":case,
                "death":death,
                "country":country,
                "link":url
        }) 
    return s
    
def source_yesterday():
    source_list=soup.find('div', {"id":"newsdate"+yesterday})
    # # source_list=soup.find('div', {"id":"news_block"})
    source_news_li = source_list.find_all("li", {"class":"news_li"})

    for row in source_news_li:
        url = ""
        death = ""
        case = ""
        country = ""
        for link in row.find_all('a', attrs={'href': re.compile("^http")}):
            url = link.get('href')
        strong=row.find_all('strong')
        z=['0' if v.text.strip() == "" else v.text.strip() for v in strong]
        for string in z:
            if ("case" in string): 
                case = string
            elif ("death" in string): 
                death = string
            else:
                country = string

        sy['Corona'].append({
                "case":case,
                "death":death,
                "country":country,
                "link":url
        }) 
    return sy
