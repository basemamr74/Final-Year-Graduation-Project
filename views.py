from django.shortcuts import render
from .models import articles

# Create your views here.

def search_article(request):
    """ search function  """
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Product.objects.filter(title__contains=query)
            return render(request, 'article-search.html', {"results":results})

    return render(request, 'article-search.html')