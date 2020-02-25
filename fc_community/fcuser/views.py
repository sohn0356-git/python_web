from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = "모든 값을 입력하셔야합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."

        else:
            fcuser = Fcuser(username=username, useremail = useremail, password=make_password(password))            
            fcuser.save()

        return render(request,'register.html',res_data)


        

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')

    else:
        form = LoginForm()
    return render(request,'login.html', {'form':form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk = user_id)
        return HttpResponse(fcuser.username)
    
    return HttpResponse("Home!")