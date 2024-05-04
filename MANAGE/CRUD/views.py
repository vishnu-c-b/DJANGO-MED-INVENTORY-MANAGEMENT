from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreateUserForm,LoginForm,Create,Update,Search
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Medicine

def HOMEPAGE(request):
    return render(request, 'HOME.html')


    
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()
            return redirect('log')

            
    else:
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'REG.html', context)


def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("inner")

    context = {'form':form}

    return render(request, 'LOGIN.html', context)


def logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("log")


@login_required(login_url='log')
def inner(request):
     records = Medicine.objects.all()
   
     return render(request, 'INNER.html',{'record': records})





@login_required(login_url='log')
def create(request):
    form=Create()
    if request.method == "POST":

        form = Create(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("inner")

    
    context={'form': form}
    return render(request, 'CREATE.html', context)


@login_required(login_url='log')
def update(request,pk):
    
        record=Medicine.objects.get(m_id=pk)

        if request.method == 'POST':

                form = Update(request.POST, instance=record)

                if form.is_valid():

                    form.save()
                    return redirect("inner")
            

        form = Update(instance=record)
        return render(request, 'UPDATE.html',{'form':form})









@login_required(login_url='log')
def delete(request,pk):
    record = Medicine.objects.get(m_id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("inner")










@login_required(login_url='log')
def search(request):
    form = Search(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Medicine.objects.filter(mname__istartswith=query)
        return render(request, 'INNER.html', {'record': results})

