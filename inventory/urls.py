from django import views
from django.contrib import admin
from django.urls import include, path
from signup.views import signaction, homeaction, aboutaction, dashboardaction, inventorytrackaction, changeaction, forgetaction, UploadPictureAction, add_item, useraction, contact,order
from login.views import loginaction, ProductList, ProductDetail, UserList, UserDetail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', signaction, name='signup'),
    path('userinfo/', useraction, name='userinfo' ),

    path('accounts/login/', loginaction, name='login'),
    path('dashboard/', dashboardaction, name='dashboard'),
    path('order/', order, name='order'),

    
    path('inventorytrack/', inventorytrackaction, name='inventorytrack'),
    path('add-item/', add_item, name='additem'),


    path('', homeaction, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('api/products/', ProductList.as_view()),
    path('api/users/', UserList.as_view()),
    path('home/aboutus/', aboutaction, name='aboutus'),
    path('home/contactus/', contact, name='contactus'),

    path('changepassword/', changeaction, name='changepassword'),
    path('forgotpassword/', forgetaction, name='forgotpassword'),
    path('profile/', UploadPictureAction, name='profile'),
    path('profile', UploadPictureAction, name='upload_picture'),

]
