from django.urls import path
from . import views


app_name = 'library'
urlpatterns = [
    path('', views.book, name ="home"),
    path('report/',views.report, name = "report"),
    path('post/', views.post, name="post"),
]