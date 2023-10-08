

from django.urls import path
from django.urls import path
from .views import loggedIn
from .import views
from django.conf import settings
from django.conf.urls.static import static
from core.views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('loggedIn', views.loggedIn, name='loggedIn'),
    path('logout', views.user_logout, name='logout'),
    path('submit_answer/logout', views.user_logout, name='logout'),
    path('start_apti', views.start_apti, name='start_apti'),
    path('apti', views.apti, name='apti'),
    # path('submit_answer', views.submit_answer, name='submit_answer'),
    path('submit_answer/<int:quest_id>', views.submit_answer, name='submit_answer')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    