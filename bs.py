# from urllib2 import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.baidu.com") 
# bsObj = BeautifulSoup(html, "html.parser")

# nameList = bsObj.findAll('input')
# for name in nameList:
#   print (name.get_text())

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html") 
bsObj = BeautifulSoup(html)
images = bsObj.findAll('img',{'src': re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image['src'])