import requests
from bs4 import BeautifulSoup

def requests_github_treding(url):
    return requests.get(url)


def extract(page):
    soup = BeautifulSoup(page.text,"html.parser")
    return soup.find_all("article")


def transform(html_repos):
    result = []
    for row in html_repos:
        name_r =''.join(row.select_one('h1.h3.lh-condensed').text.split())
        number_s = ' '.join(row.select_one('span.d-inline-block.float-sm-right').text.split())
        name_d = (row.select_one('img.avatar.mb-1.avatar-user')['alt'])
        result.append({'deverloper': name_d, 'repository_name': name_r, 'nbr_stars': number_s})
    return result

def format(repositories_data):
    result = ["Developer, Repository Name, Number of Stars"]

    for repos in repositories_data:
        row = [repos['deverloper'], repos['repository_name'], repos['nbr_stars']]
        result.append(', '.join(row))
    return "\n".join(result)

def _main():
    url = "https://github.com/trending"
    page = requests_github_treding(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos) 
    print(format(repositories_data))
    


_main()