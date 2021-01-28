import urllib

from requests_html import HTMLSession
import openpyxl
from urllib.request import Request, urlopen


def get_var_value(filename="varstore.txt"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


row = get_var_value()

id = str(4999+row)
row = str(row)

# Connect to page
url ="https://www.risingbd.com/entertainment/news/391609"   # Link of news page
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10).read()
session = HTMLSession()
r = session.get(url)


# find article
article = r.html.find('.DDetailsContent', first=True)

# find headline
headline = article.find('h1', first=True).text

# find date
date = article.find('.Ptime', first=True).text
datelist = date.split()
newdate = datelist[2] + " " + datelist[3] + " " + datelist[4]

# find details
content = r.html.find('#content-details', first=True)
details = content.find('p')
string = ""

for det in details:
    string += det.text


# find image link
imgbox = r.html.find('.DDetailsContent', first=True)
imgname = "C:\\Users\\Acer\Pictures\\5001 - 5500\\"+id+'.jpg'
imglink = imgbox.find('img', first=True)
link = imglink.attrs['src']


# header value to fake a web browser
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}


request_ = urllib.request.Request(link, None, headers) #The assembled request
response = urllib.request.urlopen(request_)
f = open(imgname, 'wb')
f.write(response.read())


# access excel file
wb = openpyxl.load_workbook("authentic.xlsx")
sheet = wb.active

# Add values
dates = "D" + row
headlines = "F" + row
detailss = "G" + row
urls = "H" + row
links = "J" + row
sheet[dates] = newdate
sheet[headlines] = headline
sheet[detailss] = string
sheet[urls] = url
sheet[links] = link

wb.save('authentic.xlsx')

print(headline)
print(newdate)
print(string)
print(link)
