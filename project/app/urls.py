from django.urls import path
from.import views


urlpatterns = [
    path('', views.homepage, name='webpage'),
    path('index', views.userreg, name='index'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('home', views.userhome, name='home'),
    path('adhome', views.dephome, name='adhome'),
    path('adlogin', views.deplogin, name='adlogin'),
    path('deplogout', views.deplogout, name='deplogout'),
    path('adreg', views.depregister, name='adreg'),
    path('userview', views.userdisplay, name='userview'),
    path('complaint', views.complaintreg, name='complaint'),
    path('complaintview', views.complaintdisplay, name='complaintview'),
    path('about', views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('support', views.support,name='support'),
    path('terms', views.terms, name='terms'),
    path('test', views.test, name='test'),
    path('delete', views.userdelete, name='delete'),
    path('update', views.update, name='update'),
    path('chps', views.changepassword, name='chps'),
    path('head', views.adminlogin, name='head'),
    path('adprofile', views.adminlogin1, name='adprofile'),
    path('signout', views.adminlogout, name='signout'),
    path('search', views.search, name='search'),
    # path('complaintview', views.complaintdisplay, name='complaintview'),





]