from django.contrib import admin
from django.urls import path, include,search_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('Ai-Advice/', include('tumor_prediction.urls')),
    path('search/', search_article, name='search_article')
]
