from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib import auth
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    if request.method == "POST" and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    return render(request, 'index.html',locals())
def about(request):
    
    return render(request, 'about.html',locals())
def news(request):
    if request.method == "POST" and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    return render(request, 'news.html',locals())
def map(request):
    num = Event.objects.all()
    if request.method == "POST"and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)

    content = {'num':num}
    return render(request, 'eventlist.html', locals())

def boothmap(request,id):
 
    num = Event.objects.get(id=id)
    if request.method == "POST" and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']       
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    if request.method == "POST"  and '商業攤一' in request.POST:#如果是以POST的方式才處理
        boothbu1 = Booth.objects.filter(event=num,number__contains='商一')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and '商業攤二' in request.POST:#如果是以POST的方式才處理
        boothbu2 = Booth.objects.filter(event=num,number__contains='商二')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and '商業攤' in request.POST:#如果是以POST的方式才處理
        boothcw = Booth.objects.filter(event=num,number__contains='商')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'A' in request.POST:#如果是以POST的方式才處理
        bootha = Booth.objects.filter(event=num,number__contains='A')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'B' in request.POST:#如果是以POST的方式才處理    
        boothb = Booth.objects.filter(event=num,number__contains='B')
        return render(request, "areamap.html", locals())    
    if request.method == "POST"  and 'C' in request.POST:#如果是以POST的方式才處理    
        boothc = Booth.objects.filter(event=num,number__contains='C')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'D' in request.POST:#如果是以POST的方式才處理    
        boothd = Booth.objects.filter(event=num,number__contains='D')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'E' in request.POST:#如果是以POST的方式才處理    
        boothe = Booth.objects.filter(event=num,number__contains='E')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'F' in request.POST:#如果是以POST的方式才處理    
        boothf = Booth.objects.filter(event=num,number__contains='F')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'G' in request.POST:#如果是以POST的方式才處理    
        boothg = Booth.objects.filter(event=num,number__contains='G')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'H' in request.POST:#如果是以POST的方式才處理    
        boothh = Booth.objects.filter(event=num,number__contains='H')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'I' in request.POST:#如果是以POST的方式才處理    
        boothi = Booth.objects.filter(event=num,number__contains='I')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'J' in request.POST:#如果是以POST的方式才處理    
        boothj = Booth.objects.filter(event=num,number__contains='J')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'K' in request.POST:#如果是以POST的方式才處理    
        boothk = Booth.objects.filter(event=num,number__contains='K')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'L' in request.POST:#如果是以POST的方式才處理    
        boothl = Booth.objects.filter(event=num,number__contains='L')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'M' in request.POST:#如果是以POST的方式才處理    
        boothm = Booth.objects.filter(event=num,number__contains='M')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'N' in request.POST:#如果是以POST的方式才處理    
        boothn = Booth.objects.filter(event=num,number__contains='N')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'O' in request.POST:#如果是以POST的方式才處理    
        bootho = Booth.objects.filter(event=num,number__contains='O')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'P' in request.POST:#如果是以POST的方式才處理    
        boothp = Booth.objects.filter(event=num,number__contains='P')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'Q' in request.POST:#如果是以POST的方式才處理    
        boothq = Booth.objects.filter(event=num,number__contains='Q')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'R' in request.POST:#如果是以POST的方式才處理    
        boothr = Booth.objects.filter(event=num,number__contains='R')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'S' in request.POST:#如果是以POST的方式才處理    
        booths = Booth.objects.filter(event=num,number__contains='S')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'T' in request.POST:#如果是以POST的方式才處理    
        bootht = Booth.objects.filter(event=num,number__contains='T')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'U' in request.POST:#如果是以POST的方式才處理    
        boothu = Booth.objects.filter(event=num,number__contains='U')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'V' in request.POST:#如果是以POST的方式才處理    
        boothv = Booth.objects.filter(event=num,number__contains='V')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'W' in request.POST:#如果是以POST的方式才處理    
        boothw = Booth.objects.filter(event=num,number__contains='W')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'X' in request.POST:#如果是以POST的方式才處理    
        boothx = Booth.objects.filter(event=num,number__contains='X')
        return render(request, "areamap.html", locals())
    if request.method == "POST"  and 'Y' in request.POST:#如果是以POST的方式才處理    
        boothy = Booth.objects.filter(event=num,number__contains='Y')
        return render(request, "areamap.html", locals())

    
    return render(request, 'map.html', locals())


def inf(request,id,pk):
    if request.method == "POST"and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    num = Event.objects.get(id=id)
    boothpk=Booth.objects.get(pk=pk)
    if request.user.is_authenticated:
        user =User.objects.get(id=request.user.id)
        love = User_Favorite_Booth.objects.filter(user=user,booth=boothpk)
    if request.method == "POST":#如果是以POST的方式才處理
        if User_Favorite_Booth.objects.filter(user=user,booth=boothpk):
            User_Favorite_Booth.objects.filter(user=user,booth=boothpk).delete()
        else:
            User_Favorite_Booth.objects.create(user=user,booth=boothpk)
        return render(request, 'information.html',locals())

    return render(request, 'information.html',locals())
@login_required
def edit(request,id,pk):
    
    num = Event.objects.get(id=id)
    boothpk=Booth.objects.get(pk=pk)
    
    if request.method == "POST":#如果是以POST的方式才處理

        boothpk.desc = request.POST['desc']
        boothpk.works_type = request.POST['workstype']
        boothpk.works_tag = request.POST['workstag']
        boothpk.rl = request.POST['url']
        #boothpk.image = request.FILES.get('ismage')
        image = request.FILES.get('image')
        if image != None:
            if image.size < 2621440:    #new!!! 限制單檔2.5MB
                boothpk.image = image

        boothpk.save()            #寫入資料庫
        return redirect(reverse('inf', args=(id,pk,)))     #重導到<index.html>網頁
    else:
        try:
            boothpk=Booth.objects.get(pk=pk)
        except:
            message = '此ID不存在'
    return render(request, "edit.html", locals())

def add(request,id):
    
    num = Event.objects.get(id=id)
    
    if request.method == "POST":#如果是以POST的方式才處理
        number = request.POST['number']
        group_name = request.POST['groupname']  #取得表單輸入資料
        desc = request.POST['desc']
        works_type = request.POST['workstype']
        works_tag = request.POST['workstag']
        Booth.objects.create(event=num,number=number, group_name=group_name,desc=desc,works_type=works_type,works_tag=works_tag).order_by('event')                     #寫入資料庫
              
    
    return render(request, "add.html", locals())

def login(request):
    next = request.GET.get('next', '')
    if request.method == "POST"and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    if request.method == "POST" and 'login'  in request.POST:

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect("/index/")
        else:
            errorms="error"
            return render(request,"login.html",locals())
    return render(request,"login.html",locals())
   

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    next = request.GET.get('next', '')
    if request.method == "POST"and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect("/index/")

    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form': form})

def search(request):

    if request.method == "POST":#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
            
    return render(request, "search.html", locals())
@login_required
def lovepage(request):
    if request.method == "POST"and 'button'  in request.POST:#如果是以POST的方式才處理
        a = request.POST['search']
          
        searchevent=Booth.objects.filter(Q(desc__contains=a)|Q(group_name__contains=a)|Q(works_type__contains=a)|Q(works_tag__contains=a)|Q(number__contains=a)).order_by('event')
        context = {'searchevent':searchevent} 
        if a :
            return render(request, "search.html", context)
    love = User_Favorite_Booth.objects.filter(user=request.user.id)


    return render(request, 'lovepage.html',locals())

@login_required
def comment(request):

    if request.method == 'POST'and 'button'  in request.POST:
        contact = request.POST.get('contact')
        user =User.objects.get(id=request.user.id)
       
        Comment.objects.create(user=user, content=contact)


    return render(request, 'contact.html', locals())