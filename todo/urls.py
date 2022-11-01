from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('show-tasks', views.show_tasks, name='show_tasks'),
    path('create-tasks', views.create_tasks, name='create_tasks'),
    path('signout', views.signout, name='signout'),
    # path('next', v♥iews.next, name='next'),

]