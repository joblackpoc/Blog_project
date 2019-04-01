# Django Python Framework
## SQLite database 0001
## Blog app + User app
 - Use Shift + Tab -> move multiple line to left
 - static -> blog -> main.css
 - template -> blog -> base.html, home.html, about.html, post_confirm_delete.html, post_detail.html, post_form.html
 - template -> users -> register.html, login.html, logout.html, profile.html
 - python manage.py makemigrations, python manage.py migrate
 - forms.py -> pip install django-crispy-forms, pip install --upgrade django-crispy-forms
 - crispy bootstrap4
 - login and logout system
 - User Profie and Picture -> pip install Pillow
 - signals.py
 - CRUD post
 
## urls.py
  from django.contrib import admin<br/>
  from django.contrib.auth import views as auth_views<br/>
  from django.urls import path, include<br/>
  from django.conf import settings<br/>
  from django.conf.urls.static import static<br/>
  from users import views as user_views<br/>
<br/>
  urlpatterns = <br/>
  [<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; path('admin/', admin.site.urls),<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path('register/', user_views.register, name='register'),<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path('profile/', user_views.profile, name='profile'),<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path('', include('blog.urls')),<br/>
 ]<br/>
<br/>
  if settings.DEBUG:<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
## forms.py<br/>
  from django import forms<br/>
  from django.contrib.auth.models import User<br/>
  from django.contrib.auth.forms import UserCreationForm<br/>
<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; class UserRegisterForm(UserCreationForm):<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; email = forms.EmailField()<br/>
<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; class Meta:<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; model = User<br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fields = ['username', 'email', 'password1', 'password2']<br/>
## setting.py<br/>
 INSTALLED_APPS = <br/>
 [<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'blog.apps.BlogConfig',<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'users.apps.UsersConfig',<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 'crispy_forms',<br/>
  STATIC_URL = '/static/'<br/>
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br/>
  MEDIA_URL = '/media/'<br/>
  CRISPY_TEMPLATE_PACK = 'bootstrap4'<br/>
  LOGIN_REDIRECT_URL = 'blog-home'<br/>
  LOGIN_URL = 'login'<br/>
## signals.py<br/>
  from django.db.models.signals import post_save<br/>
  from django.contrib.auth.models import User<br/>
  from django.dispatch import receiver<br/>
  from .models import Profile<br/>
<br/>
  @receiver(post_save, sender=User)<br/>
  def create_profile(sender, instance, created, **kwargs):<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if created:<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Profile.objects.create(user=instance)<br/>

  @receiver(post_save, sender=User)<br/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; def save_profile(sender, instance, **kwargs):<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; instance.profile.save()<br/>
