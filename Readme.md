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
  urlpatterns = <br/>[
     "tab"path('admin/', admin.site.urls),<br/>
     "tab"path('register/', user_views.register, name='register'),<br/>
     "tab"path('profile/', user_views.profile, name='profile'),<br/>
     "tab"path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),<br/>
     "tab"path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),<br/>
     "tab"path('', include('blog.urls')),<br/>
 ]<br/>
<br/>
  if settings.DEBUG:
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
## setting.py
- INSTALLED_APPS = [
    * 'blog.apps.BlogConfig',
    * 'users.apps.UsersConfig',
    * 'crispy_forms',
 - STATIC_URL = '/static/'
 - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
 - MEDIA_URL = '/media/'
 - CRISPY_TEMPLATE_PACK = 'bootstrap4'
 - LOGIN_REDIRECT_URL = 'blog-home'
 - LOGIN_URL = 'login'
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
