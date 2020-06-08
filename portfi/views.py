from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, Certificates
def home(request):
    return render(request, 'index.html')

class ProjectListView(ListView):
    model = Project
    template_name = 'work.html'
    context_object_name = 'robo'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'detail.html'

def certi(request):
    return render(request,'certi.html')

def contact(request):
    return render(request,'about.html')