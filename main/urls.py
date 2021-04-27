from django.urls import path
from main import views

urlpatterns = [
   path('Projects',views.projects,name='projects'),
   path('Language',views.language,name='language'),
   path('', views.index,name='intro')
]