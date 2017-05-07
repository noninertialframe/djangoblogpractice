"""djangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from blog.views import viewAllPosts
from blog.views import viewOnePost
from blog.views import login
from blog.views import loggedIn
from blog.views import writePost
from blog.views import editPost
from blog.views import deletePost

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', viewAllPosts, name='home'),
    url(r'^posts/(?P<pk>[0-9]+)/$', viewOnePost, name='viewOnePost'),
    url(r'^accounts/login/$', login, name='login',\
        kwargs={'template_name': 'login.html'}),
    url(r'^accounts/logout/$', auth_views.logout, name='logout',\
        kwargs={'template_name': 'logout.html'}),
    url(r'^accounts/loggedin/$', loggedIn, name='loggedin'),
    url(r'^write/$', writePost, name='writepost'),
    url(r'^posts/(?P<pk>[0-9]+)/edit/$', editPost, name='editPost'),
    url(r'^posts/(?P<pk>[0-9]+)/delete/$', deletePost, name='deletePost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
