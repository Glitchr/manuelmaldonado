from django.shortcuts import render

from .models import Repository
from .utils import get_github_credentials, sync_repos_data


def repos(request):
    """The page for my repositories"""
    try:
        username = get_github_credentials()[0]
        sync_repos_data(username)
        repos = Repository.objects.all().order_by('-updated_at')
        context = {'repos': repos}

        return render(request, 'github/projects.html', context)
    except Exception as e:
        print(e)

        return render(request, 'github/error.html', {'error_message': str(e)})
