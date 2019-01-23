from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
USER_DICT = {
    '1':{'name':'root1','email':'root@123'},
    '2': {'name': 'roo2t', 'email': 'root@123'},
    '3': {'name': 'root3', 'email': 'root@123'},
    '4': {'name': 'root4', 'email': 'root@123'},
    '5': {'name': 'roo5t', 'email': 'root@123'},

}

def detail(request,nid):
    #nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})



def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})

'''
def login(request):

    if request.method =="GET":
        return render(request,'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u =='pjj' and p == '123':
            return redirect('/index/')
    else:
         return render(request,'/index/',)
    '''



from app01 import models
def orm(request):
    #增加数据
    #models.UserIfor.objects.create( username = 'root',password = '123' )

   # dic = { 'username':'pjj','password':'123'}
    #models.UserIfor.objects.create(**dic)

    #obj = models.UserIfor(username = 'root1',password = '123')
    #obj.save ()

    #查询
    result = models.UserIfor.objects.all()
    print(result)

def login(request):

    if request.method =="GET":
        return render(request,'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserIfor.objects.filter(username=u,password=p)
        return render(request,'login.html')

       ''' v = request.POST.get('gender')
        c = request.POST.getlist('favor')
        f  = request.FILES.get('fafafa')
        import os
        file_path = os.path.join('upload',f.name)
        f1 = open(file_path,mode="wb")
        for i in f.chunks():
            f.write(i)
        f1.close()
        print(f)


        '''


from django.views import View

class Home(View):

    def dispatch(self, request, *args, **kwargs):
        rsule = super(Home,self).dispatch(request,*args,**kwargs)
        return rsule


    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method,'POST')
        return render(request, 'home.html')


