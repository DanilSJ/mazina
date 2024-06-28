from django.contrib import admin
from django.urls import path
from main.views import index, shorts, shirt, sneakers, buy_shirt, buy_shorts, buy_sneakers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shorts/', shorts, name='shorts'),
    path('shirt/', shirt, name='shirt'),
    path('sneakers/', sneakers, name='sneakers'),
    path('buy/shirt/<int:pk>/', buy_shirt, name='buy_shirt'),
    path('buy/shorts/<int:pk>/', buy_shorts, name='buy_shorts'),
    path('buy/sneakers/<int:pk>/', buy_sneakers, name='buy_sneakers'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)