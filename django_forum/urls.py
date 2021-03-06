"""django_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import django
from django.conf.urls import url,include
from django.contrib import admin
import view
from comment.views import *
from message.views import *
from userprofile.views import *




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^static/(?p<path>.*)s',django.contrib.staticfiles.views.serve),            #定义这样的路径调用自定类按照静态文件处理
    url(r'^$', view.index),
    url(r'^fb', view.fb),
    url(r'^home',view.home),
    url(r'^logo/',logo),
    url(r'^article/',include('article.urls')),
    url(r'^register/',include('user.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^comment/create/', comment_create),
    url(r'^message/',include('message.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    # url(r'^accounts/login/$',  login, {'template_name': 'registration/login.html'}),   # 指定登录页面模板
    # url(r'^accounts/logout/$', logout_then_login),


]
