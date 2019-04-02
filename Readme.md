# Django Python Framework
## SQLite database 0001
## Blog app + User app
 - Use Shift + Tab -> move multiple line to left
 - static -> blog -> main.css
 - template -> blog -> base.html, home.html, about.html, post_confirm_delete.html, post_detail.html, post_form.html, user_posts.html
 - template -> users -> register.html, login.html, logout.html, profile.html, password_reset.html, password_reset_done.html, password_reset_confirm.html, password_reset_complete.html
 - python manage.py makemigrations, python manage.py migrate
 - forms.py -> pip install django-crispy-forms, pip install --upgrade django-crispy-forms
 - crispy bootstrap4
 - login and logout system
 - User Profie and Picture -> pip install Pillow
 - signals.py
 - CRUD post
 - Paginator -> user_posts.html
 - Password reset by Email (gmail Apps Password sign in)
 - pip install virtualenv
 - heroku login
 - pip install gunicorn
 - virtualenv name
 - run -> "C:\Blog\Blog_project\blog_project\Scripts\activate.bat"
 - pip install pandas
 - pip freeze > requirement.txt
 - git init
 - .gitignore
 - git add -A
 - git commit -m "Initial Commit"
 - heroku create appname -> https:appname.herokuapp.com
 - heroku buildpacks:set heroku/python
 - git push heroku master

 
## urls.py
 - from django.contrib import admin
 - from django.contrib.auth import views as auth_views
 - from django.urls import path, include
 - from django.conf import settings
 - from django.conf.urls.static import static
 - from users import views as user_views

 - urlpatterns = [
    * path('admin/', admin.site.urls),
    * path('register/', user_views.register, name='register'),
    * path('profile/', user_views.profile, name='profile'),
    * path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    * path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    * path('', include('blog.urls')),
* ]

 - if settings.DEBUG:
    * urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
## forms.py
 - from django import forms
 - from django.contrib.auth.models import User
 - from django.contrib.auth.forms import UserCreationForm

 - class UserRegisterForm(UserCreationForm):
   * email = forms.EmailField()

  - class Meta:
     * model = User
     * fields = ['username', 'email', 'password1', 'password2']

## signals.py
 - from django.db.models.signals import post_save
 - from django.contrib.auth.models import User
 - from django.dispatch import receiver
 - from .models import Profile

 - @receiver(post_save, sender=User)
 - def create_profile(sender, instance, created, **kwargs):
    * if created:
        * Profile.objects.create(user=instance)

 - @receiver(post_save, sender=User)
 - def save_profile(sender, instance, **kwargs):
    * instance.profile.save()
