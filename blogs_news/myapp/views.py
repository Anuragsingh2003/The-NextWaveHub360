from .forms import BlogForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
import requests
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

def index(request):
    return render(request, 'index.html')


class BlogListView(UserPassesTestMixin, generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You need to be logged in as an admin to access this page.')
        return redirect('user_login')  

class BlogCRUDView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You need to be logged in as an admin to access this page.')
        return redirect('user_login')  # Replace 'your_login_url' with your actual login URL.

class Createblog(UserPassesTestMixin, generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You need to be logged in as an admin to access this page.')
        return redirect('user_login')  # Replace 'your_login_url' with your actual login URL.

    
    

# views.py
from decouple import config
from django.shortcuts import render, redirect

def news_list(request):
    if request.user.is_authenticated:
        api_url = 'https://newsapi.org/v2/top-headlines'
        api_key = config('NEWS_API_KEY')
        params = {'country': 'us', 'apiKey': api_key}
        
        response = requests.get(api_url, params=params)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            news_articles = response.json()['articles']
            context = {'news_articles': news_articles}
            return render(request, 'news_list.html', context)
        else:
            # Handle the case where the request was not successful
            error_message = f"Error: {response.status_code} - {response.text}"
            context = {'error_message': error_message}
            return render(request, 'error.html', context)
    else:
        return redirect('user_login')



# @login_required
def news_detail(request, article_id):
    if request.user.is_authenticated:
        article = get_object_or_404(NewsArticle, id=article_id)
        context = {'article': article}
        return render(request, 'news_detail.html', context)
    else:
            return redirect(user_login)


# @login_required
def blog_list(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(author=request.user)
        context = {'blogs': blogs,'user': request.user}
        return render(request, 'Blogs_list.html', context)
    else:
        return redirect(user_login)


# @login_required
def AllBlogList(request):
    if request.user.is_authenticated:    
        AllBlogs=Blog.objects.all()
        data={"AllBlogs":AllBlogs}
        # injected all db data in sorm of dic data use by name AllBlogs in html file
        return render(request,"AllBlog.html",data)
    else:
        return redirect(user_login)



#geting id from allblog html file url btn

# @login_required
def blog_detail(request, blog_id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'blogs_details.html', {'blog': blog})
    else:
        return redirect(user_login)





# @login_required
def blog_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.save()
                return redirect('blog_list')
        else:
            form = BlogForm()
        context = {'form': form ,'user': request.user}
        return render(request, 'blog_form.html', context)
    else:
        return redirect(user_login)





# @login_required
def blog_delete(request, blog_id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, id=blog_id)
        if request.method=='POST':
            if blog.author == request.user:
                blog.delete()
            return redirect('blog_list')
        return render(request,'blog_delete.html',{'blog':blog})
    else:
        return redirect(user_login)


# @login_required
def edit_blog(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    if request.method=='POST':
        blog=BlogForm(request.POST,instance=blog)
        if blog.is_valid:
            blog.save()
            return redirect('blog_list')
    else:
        blog=BlogForm(instance=blog)

    return render(request,'editblog.html',{'blog':blog})

from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


# @login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=form.save()
            user = authenticate(request, username=username, password=password) # for login   
            #this line makes the error - bcz login authenticn not working nd also ther is no need to use..  
            login(request,user)    
            messages.success(request, f'Account created for {username}!')
            return redirect('user_login')# redirecting to login func for users
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})






def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # checking basic or minimum reqirment to proceed that rules created by django auth inbuilt
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # actual checks that usr availble or not or pswd corrt
            if user is not None: # if all things are correct then go to main pg
                login(request, user)
                return redirect('news_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logt(request):
    logout(request)
    return redirect('index')


def admin_sec(request):
    return render(request, 'admin_sec.html')


def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # checking basic or minimum reqirment to proceed that rules created by django auth inbuilt
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) # actual checks that usr availble or not or pswd corrt
            if user is not None and user.is_staff: # if all things are correct then go to main pg
                login(request, user)
                return redirect('admin_sec')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

