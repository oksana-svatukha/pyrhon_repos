#Візуалізація репозиторіїв у Plotly

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Зробити виклик черз Api та зберегти відповідь.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

#Обробити результати.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

#Зробити візуалізацію.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(254, 205, 223)',
        'line': {'width': 1.3, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.75,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')