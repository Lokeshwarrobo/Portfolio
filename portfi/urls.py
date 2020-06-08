from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('work/',views.ProjectListView.as_view(),name='work'),
    path('detail/<int:pk>/',views.ProjectDetailView.as_view(),name='detail'),
    path('certi/',views.certi,name='certi'),
    path('lokeshwar/about/',views.contact, name = 'about')

]