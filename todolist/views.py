from asyncio import tasks
                            
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Task 


#start login pageview
class Customeloginview(LoginView):
    template_name='todolist/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('heompage')

#end login pageview

#start register pageview
class registerpage(FormView):
    template_name='todolist/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('heompage')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(registerpage,self).form_valid(form)
       
#end register pageview


#homepage
class Tasklist(LoginRequiredMixin, ListView):
    model=Task
    context_object_name='tasks'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        return context

#end homepage


#start detaillist views

class TaskDeatil(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name='task'
    template_name='todolist/task.html'

#end detaillist views


#start create pageview
class Cretetask(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('heompage')
    template_name='todolist/create.html'
#end create pageview


#start updatepage view
class Updatetask(LoginRequiredMixin, UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('heompage')
    template_name='todolist/create.html'
    

#end updatepage view


#start deletepage view
class Deletetask(LoginRequiredMixin, DeleteView):
    model=Task
    context_object_name='tasks'
    success_url=reverse_lazy('heompage')
    
#end deletepage view



