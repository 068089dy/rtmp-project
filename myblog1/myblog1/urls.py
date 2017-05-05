"""myblog1 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
import article.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #首页
    url(r'^$',article.views.home),
    #登录
    url(r'^login',article.views.login),
    #注册
    url(r'^registe',article.views.registe),
    #注册
    url(r'^registe/re',article.views.registere),
    #获取主播介绍
    url(r'^get_anchor_data/',article.views.get_anchor_data),
    #提交主播介绍
    url(r'^commit_anchor_data/',article.views.commit_anchor_data),
    #直播测试
    url(r'^livetest',article.views.livetest),

    #app下载
    url(r'^app',article.views.app),
    #后缀
    url(r'^([a-z，0-9]+)/$', article.views.detail, name='detail'),
    #测试
    url(r'^test/',article.views.test),
]
