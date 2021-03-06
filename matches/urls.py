from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'matches'
urlpatterns = [
    path('all_matches/', all_matches, name='all-matches'),
    path('load_excel/', load_excel, name='load-excel'),
    path('delete/', delete, name='delete-all'),
    path('filters/', filters, name='filters'),
    path('add_match/', add_match, name='add-match'),
    path('', index, name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)