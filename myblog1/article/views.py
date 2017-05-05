from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators import csrf
# 引入我们创建的表单类
from .forms import AddForm
# 引入model
from article.models import Anchor
# Create your views here.
#首页
def home(request):
    return render(request, 'index.html', {'current_time': datetime.now()})

#登录
def login(request) :
    if request.method == 'POST':# 当提交表单时
        u = request.POST['u']
        p = request.POST['p']
        return HttpResponse("user"+u+" "+"password:"+p)

    else:# 当正常访问时
        return render(request, 'login.html', {'current_time': datetime.now()})

#注册
def registe(request):
    return HttpResponse("registe")
def registere(request):
    return HttpResponse("registere")

#获取主播介绍
def get_anchor_data(request):
    if request.POST:
        post_id = request.POST['id']

        if Anchor.objects.get(id = post_id):
            object = Anchor.objects.get(id = post_id)
            head_img_src = object.head_img_src
            name = object.name
            content = object.content
            json = "{\"head_img_src\":\""+head_img_src+"\",\"name\":\""+name+"\",\"content\":\""+content+"\"}"
            return HttpResponse(json)
        else:
            return HttpResponse("null")
    else:
        return render(request, 'login.html', {'current_time': datetime.now()})

#提交主播介绍
def commit_anchor_data(request):
    return HttpResponse("commit_anchor_data")

#直播测试
def livetest(request):

    if request.POST:
        passwd = request.POST['pass']
        user = request.POST['name']
        if passwd=="password" and user=="test":
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

    else:
        return HttpResponse(status=404)


#app下载
def app(request):
    return render(request, "app.html")

#后缀
def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)

#测试
def test(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
