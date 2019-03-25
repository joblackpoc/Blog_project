# Django Python Framework
## SQLite database 0001
## Blog app + User app
 - static -> blog -> main.css
 - template -> blog -> base.html, home.html, about.html
 - template -> users -> register.html, login.html, logout.html, profile.html
 - python manage.py makemigrations, python manage.py migrate
 - forms.py -> pip install django-crispy-forms, pip install --upgrade django-crispy-forms
 - crispy bootstrap4
 - login and logout system
 - User Profie and Picture
 - pip install Pillow
 - signals.py
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
        ** Profile.objects.create(user=instance)

 - @receiver(post_save, sender=User)
 - def save_profile(sender, instance, **kwargs):
    * instance.profile.save()
