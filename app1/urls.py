from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('bookadd/',views.bookadd,name='bookadd'),
    path('bookremove/<int:id>',views.bookremove,name='bookremove'),
    path('staff/',views.staff,name='staff'),
    path('student/',views.student,name='student'),
    path('get/<int:id>',views.get,name='get'),
    path('returned/<int:id>',views.returned,name='returned'),
    path('returned_items/',views.returned_items,name='returned_items'),
    path('signout',views.signout,name='signout'),
]
