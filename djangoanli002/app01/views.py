from django.shortcuts import render
from app01 import models
from django.shortcuts import redirect
# Create your views here.
from django.shortcuts import HttpResponse
def business(request):
    v1 = models.Business.objects.all()

    v2 = models.Business.objects.all().values('id','caption')

    v3 = models.Business.objects.all().values_list('id', 'caption')
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})

def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        for row in v1:
            print(row.nid,row.hostname,row.ip,row.port,row.b.caption,row.b.code)
        v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        for row in v2:
            print(row['nid'],row['hostname'],row['b__caption'])
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')
        b_list = models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})
    elif request.method == "POST":
        print(125415)
        h = request.POST.get('hostname')
        i = request.POST.get('IP')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        print(h,i,p)
        models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        return redirect('/host')

def test_ajax(request):
    import json
    ret={'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h)>5:
            models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
        else:
            ret['status'] = False
            ret['error'] = "太短了"
    except:
        ret['status'] = False
        ret['error'] = "请求错误"
    return HttpResponse(json.dumps(ret))


