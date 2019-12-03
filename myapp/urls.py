from django.urls import path
from myapp import views

app_name="myapp"
urlpatterns = [
    path('',views.index,name="index"),
    path('child1/',views.Child1,name="child1"),
    path('child2/',views.Child2,name="child2"),
    path("form/",views.Form_demo,name="form_demo")
]
