from django.shortcuts import render, HttpResponseRedirect
from student.models import User
from student.forms import StudentRegistration
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.
class UserAddShowView(TemplateView):
    template_name = 'Djcrudclass/home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu':stud,'form':fm}
        return context
     
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          name =  fm.cleaned_data['name']
          email =  fm.cleaned_data['email']
          password =  fm.cleaned_data['password']
          reg = User(name=name,email=email,password=password)
          reg.save()
          return HttpResponseRedirect('/')
    


class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self,*args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
        


class UserUpdateView(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'Djcrudfun/update.html',{'form':fm})
    
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request, 'Djcrudfun/update.html',{'form':fm})
    
