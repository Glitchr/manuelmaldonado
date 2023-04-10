from django.shortcuts import render

from .models import Repository
from .utils import sync_repos_data


def repos(request):
    """The page for my repositories"""
    try:
        sync_repos_data()
        repos = Repository.objects.all().order_by('-pushed_at')
        context = {'repos': repos}

        return render(request, 'github/projects.html', context)
    except Exception as e:
        print(e)

        return render(request, 'github/error.html', {'error_message': str(e)})
