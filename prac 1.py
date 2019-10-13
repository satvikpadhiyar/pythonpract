# import requests
# from bs4 import BeautifulSoup
# import re
# URL = "http://charusat.edu.in/"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html.parser')
# img_tags = soup.find_all('img')
# urls = [img['src'] for img in img_tags]
# print(urls)
# for url in urls:
#     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
#     with open(filename.group(1), 'wb') as f:
#         if 'http' not in url:
#             # sometimes an image source can be relative
#             # if it is provide the base url which also happens
#             # to be the site variable atm.
#             url = '{}{}'.format(URL, url)
#         response = requests.get(url)
#         f.write(response.content)
from bs4 import BeautifulSoup
import requests
import re
URL = "http://charusat.edu.in"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
img = soup.find_all('img')
urls = [i["src"] for i in img]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    # # filename = re.search(r'/([\w-_]+[.](jpg|gif|png))$', url)
    print(filename.group(2))
    # with open(filename.group(1), 'wb') as f:
    #     if 'http' not in url:
    #         url = '{}{}'.format(URL, url)
    #     response = requests.get(url)
    #     f.write(response.content)
