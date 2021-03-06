import requests
from bs4 import BeautifulSoup
import re
import sys

base_url = "http://openaccess.thecvf.com/content_cvpr_" + sys.argv[1] +"/papers/"
page = requests.get(base_url)
soup = BeautifulSoup(page.text,'lxml')
paper_list_a = soup.find_all('a')
paper_list = []
for paper_a in paper_list_a:
    paper_list += [paper_a.get('href')]

for paper in paper_list:
    if None != re.search(r"pdf", paper):
        url = base_url + paper
        file = requests.get(url)
        with open(paper, "wb") as f:
            f.write(file.content)
