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





















def tpl1(request):
    user_list =[1,2,3]
    return render(request,'tpl1.html',{'u':user_list})


def tpl2(request):
    name = 'root'
    return render(request, 'tpl2.html', {'name': name})


def tpl3(request):
    pas = 'root'
    return render(request, 'tpl3.html', {'pass': pas})
def tpl4(request):
    name = 'csafawveggDDDFGGEED'
    return render(request, 'tpl4.html', {'name': name})

from django.utils.safestring import mark_safe
LIST = []
for i in range(555):
    LIST.append(i)
def user_list(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    start = (current_page-1)*10
    end = current_page*10
    data = LIST[start:end]
    all_count = len(LIST)
    total_count,y= divmod(all_count,10)
    if y:
        total_count+=1
    page_list = []
    start_index = current_page-5
    end_index = current_page+5+1
    if total_count<11:
        start_index =1
        end_index = total_count+1
    else:
        if current_page<=6:
            start_index =1
            end_index = 11+1
        else:
            start_index = current_page-5
            end_index = current_page+5+1
            if (current_page+5)>total_count:
                end_index = total_count+1
                start_index = total_count-11+1



    for i in range(start_index,end_index):
        if i == current_page:
            temp = '<a class = "page active" href="/user_list/?p=%s">%s</a>' % (i, i)
        else:
            temp = '<a class = "page" href="/user_list/?p=%s">%s</a>'%(i,i)
        page_list.append(temp)


    page_str = "".join(page_list)
    page_str = mark_safe(page_str)
    return render(request,'user_list.html',{'li':data,"page_str":page_str})
