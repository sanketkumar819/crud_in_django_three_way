from django.shortcuts import render, HttpResponseRedirect
from student.models import User
from student.forms import StudentRegistration

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          name =  fm.cleaned_data['name']
          email =  fm.cleaned_data['email']
          password =  fm.cleaned_data['password']
          reg = User(name=name,email=email,password=password)
          reg.save()
          fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
        
    return render(request, 'Djcrudfun/home.html',{'form':fm,'stu':stud})
 
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/fbv')
 
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'Djcrudfun/update.html',{'form':fm})