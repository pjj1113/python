from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
# Create your views here.
USER_DICT = {
    '1':{'name':'root0','email':'12151'},
    '2':{'name': 'root1', 'email': '12151'},
    '3':{'name': 'root2', 'email': '12151'},
    '4':{'name': 'root3', 'email': '12151'},
    '5':{'name': 'root4', 'email': '12151'},
}

USER_LIST = {
    'k1':'root',
    'k2':'root2',
    'k3':'root3',
    'k4':'root4',

}

def index(request):
    return render(request,'index.html')

def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        print(user_info)
        return render(request,"user_info.html",{"user_list":user_list})
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username =u,password=p)
        user_list = models.UserInfo.objects.all()
        return render(request,'user_info.html',{"user_list":user_list})
def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/cmdb/user_info/")


def user_edit(request,nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id = nid).first()
        return render(request,'user_edit.html',{'obj':obj})
    elif request.method == 'POST':
        uid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=uid).update(username=u,password = p)
        return redirect('/cmdb/user_info/')

def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id = nid).first()
    #models.UserInfo.objects.get(id=nid)
    return render(request,'user_detail.html',{'obj':obj})


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method=="POST":
        #数据库中执行select *form user
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u, password=p)
        print(obj)
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request,'login.html')

        return render(request, "login.html")
    else:
        return redirect("/index/")

from app01 import models
def orm(request):
    u = request.POST.get('user')
    p = request.POST.get('pwd')
    obj = models.UserInfo.objects.filter(username=u,password=p)
    print(obj)
    #创建
   # models.UserInfo.objects.create(username = 'root',password = '123')
    #obj = models.UserInfo(username ='pjj',password = '1234')
   # obj.save()
    #查
   # result = models.UserInfo.objects.all()
   # result = models.UserInfo.objects.filter(username='root',password='123')
    #print(result)
    #删除
    #models.UserInfo.objects.filter(username='root').delete()
    #更新
   # models.UserInfo.objects.all().update(password = 123)

    return HttpResponse('orc')


def home(request):
    return HttpResponse("home")


from django.views import View
class Home(View):

    def dispatch(self, request, *args, **kwargs):
        result = super(Home,self).dispatch(request,*args,**kwargs)
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method)
        return render(request, 'home.html')
'''
def detail(request):
    nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    print(detail_info)
    return render(request,'detail.html',{'detail_imfo':detail_info})'''

def detail(request,nid):
    print(request)
    detail_info = USER_DICT[nid]
    print(detail_info)
    return render(request, 'detail.html', {'detail_info': detail_info})




"""
login原始代码

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method=="POST":

        a = request.POST.get("gender")
        print(a)
        return render(request, "login.html")
    else:
        return redirect("/index/")


"""