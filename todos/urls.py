from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
	path('',views.index,name='index'),
	path('add',views.addTodo,name='add'),
	path('deleted/<int:todos_id>',views.deleted,name='deleted'),
]