from django.shortcuts import render
from .models import articles

# Create your views here.

def search_article(request):
    """ search function  """
    if request.method == "GET":
        query = request.GET.get('title','content', None)
         submitbutton= request.GET.get('submit')
        if query:
            results = Product.objects.filter(title__icontains=query).distinct() | (content__icontains=query).distinct()
            return render(request, 'article-search.html', {'results':results,'submitbutton': submitbutton})

    return render(request, 'article-search.html')
