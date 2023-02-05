from django.urls import path
from . import views
#авторизация
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', login_required(views.index), name = 'home'),
    path('search', login_required(views.search), name='searchquery'),
    path('switchlist', login_required(views.switches), name = 'switchlist'),
    path('api/pingget', views.pingget, name = 'pingget'),
    path('api/pingdetail', views.pingdetail, name = 'pingdetail'),
    path('createsw', login_required(views.createsw), name = 'createsw'),
    path('createcat', login_required(views.createcat), name = 'createcat'),
    path('createtit', login_required(views.createtit), name = 'createtit'),
    path('switchlist/<int:pk>', login_required(views.swdetail), name='swdetail'),
    path('switchlist/editsw/<int:id>', views.editsw, name='editsw'),
    path('switchlist/delete/<int:id>', views.deleteswitch, name='deleteswitch'),
    path('switchlist/editcat/<int:id>', views.editcat, name='editcat'),
    path('switchlist/deletecat/<int:id>', views.deletecat, name='deletecat'),
    path('switchlist/edittit/<int:id>', views.edittit, name='edittit'),
    path('switchlist/deletetit/<int:id>', views.deletetit, name='deletetit'),
    path('backupjs', views.backupjs, name='backupjs'),
    path('category', login_required(views.category), name='category'),
    path('category/<int:pk>', login_required(views.catdetail), name='catdetail'),
    path('tituls', login_required(views.tituls), name='tituls'),
    path('tituls/<int:pk>', login_required(views.titdetail), name='titdetail'),
    path('autodata/<int:pk>', views.autodata, name='autodata'),
    path('api/getconfig', views.getconfig, name='getconfig'),
    path('onlybad', views.onlybad, name='onlybad'),
    path('backup', views.backup, name='backup'),

    path('create_backup/<int:pk>', views.create_backup, name='create_backup'),
    path('delete_backup/<int:pk>', views.delete_backup, name='delete_backup'),
    path('update_backup/<int:pk>', views.update_backup, name='update_backup'),



]
