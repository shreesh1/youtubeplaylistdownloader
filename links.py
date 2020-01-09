import requests
import sys
from bs4 import BeautifulSoup
url = sys.argv[1]
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
aaa = soup.find_all('a',attrs={'class':'pl-video-title-link'})
print(aaa)
