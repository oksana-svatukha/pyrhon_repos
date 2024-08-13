import requests

# Зробти виклик через API та зберегти відповідь.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

#Зберегти відповідь API у змінну.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

"""# Обробити результати.
print(responce_dict.keys())"""

# Дослідити інфрмацію щодо репозиторіїв.
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

"""#Дослідити перший репозиторій.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")"""
"""for key in sorted(repo_dict.keys()):
    print(key)"""

print('\nSelected information about each repository:')
"""print("\nSelected information about first repository:")"""
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner'], ['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

#Обмеження Api на кількість запитів

"https://api.github.com/rate_limit"

