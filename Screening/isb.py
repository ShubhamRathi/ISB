import requests
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

patent_no ='8829700'
url="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=1&p=1&f=G&l=50&d=PTXT&S1=8829700&OS=8829700&RS=8829700%22,%228829700_patent_dwd.html"

# Scraping and shaping the excel file

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
field1 = "Inventors:"
field2 = "Assignee:"
field3 = "Filed:"

for i in soup.find_all('th'):
    if i.string:
        tag = i.string.strip()
        if field1 == tag:
            inv = (i.find_next_sibling('td').text).split(")',")
            re.sub('[^A-Za-z0-9]+', '', inv[0])
            loc=str(inv).split("),")
        if field2 == tag:                   # Assignee
            asg=i.find_next_sibling('td').text# Assignee Text String
            asg=asg[0:asg.find('(')].strip()
        if field3 == tag:                   # Filed
            filed= i.find_next_sibling('td').text # Filed Text String


# Creating the excel file

wb=Workbook()
sheet1=wb.add_sheet('Sheet 1')

# Populating the excel file

sheet1.write(0,0,'Pat_num') # Add Patent Num
sheet1.write(1,0,patent_no)

sheet1.write(0,1,field3[:-1]) # Add Filed
sheet1.write(1,1,filed)

sheet1.write(0,2,field2[:-1]) # Add Assignee
sheet1.write(1,2,asg)

ev=4
odd=3
for i in xrange(1,len(loc)+1): # Add Inv, Loc
	wr=str(loc[i-1]).strip()
	rep=["[","u'","\\n","']", ")"]
	for r in rep:
		wr=wr.replace(r,"")
	sheet1.write(0,ev,"Loc"+str(i))
	sheet1.write(1,ev,wr[wr.find('(')+1:].strip())
	ev=ev+2
	sheet1.write(0,odd,"Inv"+str(i))
	sheet1.write(1,odd,wr[0:wr.find('(')].strip())
	odd=odd+2
wb.save('ISB_Strat_Assignement_Patent.xlsx')