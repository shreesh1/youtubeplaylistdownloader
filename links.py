import requests
from bs4 import BeautifulSoup
url = "https://www.youtube.com/playlist?list=PLyWJk75qqUWmLIocImpaqgLte9iIz1tKf"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
aaa = soup.find_all('a',attrs={'class':'pl-video-title-link'})
print(aaa)
