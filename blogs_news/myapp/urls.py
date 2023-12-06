from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import BlogListView, BlogCRUDView,Createblog

urlpatterns = [
    # admin sec api urls..............................................
    path('Bloglist_admin/', BlogListView.as_view(), name='BlogListView'),
    path('Createblog/', Createblog.as_view(), name='Createblog'),
    path('blog_crud_admin/<int:pk>/', BlogCRUDView.as_view(), name='BlogCRUDView'),
    #user urls........................................................
    path('', views.index, name='index'),
    path('news_list/', views.news_list, name='news_list'),
    path('register/', register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_sec/', views.admin_sec, name='admin_sec'),
    path('admin_login/', views.user_login, name='user_login'),
    path('logt/', views.logt, name='logt'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('news/<int:article_id>/', views.news_detail, name='news_detail'),
    path('bloglist/', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('blog/<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
    path('blog/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('allblg/', views.AllBlogList, name='AllBlogList'),
    #user password auth urls.....................................................................................................
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


