import requests
from bs4 import BeautifulSoup

G_PREFIX = "[好雷]"
N_PREFIX = "[普雷]"
B_PREFIX = "[負雷]"

output = {G_PREFIX: [], N_PREFIX: [], B_PREFIX: []}
iteration = 0
url_prefix = "https://www.ptt.cc"
url = url_prefix + "/bbs/movie/index.html"

while iteration < 10:
    print(iteration, url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div_titles = soup.find_all("div", class_ = "title")

    for div_title in div_titles:
        if div_title.select_one("a") is None:
            continue
        title = div_title.select_one("a").getText()
        if title.startswith(G_PREFIX):
            output[G_PREFIX].append(title)
        elif title.startswith(N_PREFIX):
            output[N_PREFIX].append(title)
        elif title.startswith(B_PREFIX):
            output[B_PREFIX].append(title)

    iteration += 1
    
    div_paging = soup.find("div", class_ = "btn-group-paging")
    paging_elements = div_paging.find_all("a")
    for paging_element in paging_elements:
        if '上頁' in paging_element.getText():
            url = url_prefix + paging_element.get('href')

with open('movie.txt', 'w') as f:
    f.write('\n'.join(output[G_PREFIX]))
    f.write('\n'.join(output[N_PREFIX]))
    f.write('\n'.join(output[B_PREFIX]))