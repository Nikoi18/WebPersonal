#Encargado de manejar las direciones de la web

from django.contrib import admin
from django.urls import path
from core import views as core
from django.conf import settings
from portfolio import views as port




urlpatterns = [
    path('', core.home, name='home'),
    path('about-me/', core.about, name='about'),
    path('portfolio/', port.portfolio, name='portfolio'),
    path('contact/', core.contact, name='contact'),
    path('admin/', admin.site.urls),  
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)