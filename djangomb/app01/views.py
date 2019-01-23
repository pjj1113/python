from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
def login(request):
    if request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        yz = models.User.objects.filter(username=u,password=p).first()
        if yz:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("登陆失败")
    return render(request,"login.html")