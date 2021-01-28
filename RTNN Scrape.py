import urllib

from requests_html import HTMLSession
import openpyxl
from urllib.request import Request, urlopen


# Auto increment variable value
def get_var_value(filename="varstore.txt"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


row = get_var_value()

# Assign ID
id = str(4999+row)
row = str(row)

# Connect to page
url = "https://www.risingbd.com/national/news/391537"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

session = HTMLSession()
r = session.get(url)

# find article
article = r.html.find('.simpleCall', first=True)

# find headline
headline = article.find('h2', first=True).text

# find date
date = article.find('span', first=True).text

# find details
content = r.html.find('.detail-content', first=True)
details = content.find('p')
string = ""

for det in details:
    string += det.text

# find image link
imgname = "C:\\Users\\Acer\Pictures\\5001 - 5500\\"+id+'.jpg'
imglink = content.find('img', first=True)
link = imglink.attrs['src']
urllib.request.urlretrieve(link, imgname)

# access excel file
wb = openpyxl.load_workbook("authentic.xlsx")
sheet = wb.active

# Add values
dates = "D" + row
headlines = "F" + row
detailss = "G" + row
urls = "H" + row
links = "J" + row

sheet[dates] = date
sheet[headlines] = headline
sheet[detailss] = string
sheet[urls] = url
sheet[links] = link

wb.save('authentic.xlsx')

print(headline)
print(date)
print(string)
print(link)
