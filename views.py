from django.shortcuts import render,redirect
from .forms import signupform
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signupform()
    return render(request,'signup.html',{'form':form})

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render('next')
    else:
        return render(request,'login.html')

def Next(request):
    return render(request,'next.html')