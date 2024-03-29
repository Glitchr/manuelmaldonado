import requests
from decouple import config
    

def get_github_headers():
    """Function to set up headers for authentication"""
    token = config('G_TOKEN')
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'}
     
    return headers


def get_github_data(endpoint):
    """Function to make a GET request to Github API"""
    GITHUB_API_URL = 'https://api.github.com'
    headers = get_github_headers()
    response = requests.get(f'{GITHUB_API_URL}{endpoint}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Github API error: {response.status_code}')


def sync_repos_data():
    """
    Function to create or update Repository objects for each repo
    returned by the Github API
    """
    repos_data = get_github_data(f'/user/repos')

    from .models import Repository

    for repo in repos_data:
        repository, created = Repository.objects.get_or_create(
            name=repo['name'],
            defaults={
                'description': repo['description'],
                'link': repo['html_url'],
                'is_public': not repo['private'],
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
                'pushed_at': repo['pushed_at']})

        # If the repository already exists, update its fields with the latest
        # data from the Github API
        if not created:
            repository.description = repo['description']
            repository.link = repo['html_url']
            repository.is_public = not repo['private']
            repository.created_at = repo['created_at']
            repository.updated_at = repo['updated_at']
            repository.pushed_at = repo['pushed_at']
            repository.save()
