import requests
from bs4 import BeautifulSoup


def get_posts(num_of_pages=1, min_upvotes=1):
    posts = []
    for i in range(num_of_pages):
        res = requests.get(f'https://news.ycombinator.com/news?p={i+1}')
        soup = BeautifulSoup(res.text, 'html.parser')

        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        posts = posts + create_page_post_list(links, subtext, min_upvotes)

    return posts


def create_page_post_list(links, subtext, min_upvotes):
    post_list = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        upvotes = subtext[index].select('.score')
        if len(upvotes):
            points = int(upvotes[0].getText().replace(' points', ''))
            if points > min_upvotes:
                post_list.append(
                    {'title': title, 'link': href, 'votes': points})
    return sorted(post_list, key=lambda item: item['votes'], reverse=True)
