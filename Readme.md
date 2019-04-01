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
 - Paginator
 *user_posts.html
**{% extends 'blog/base.html' %}
**{% block content %}
  **<h1 class="mb-3">Post by {{ view.kwargs.username }} ({{ page_obj.paginator.count }})</h1>
    **{% for post in posts %}
      **<article class="media content-section">
        **<img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
          **<div class="media-body">
            **<div class="article-metadata">
              **<a class="mr-2" href="{% url 'user-posts' post.author.username %}">{{ post.author }}</a>
              **<small class="text-muted">{{ post.date_posted|date:"d F Y, H:i" }}</small>
            **</div>
            **<h2><a class="article-title" href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
            **<p class="article-content">{{ post.content }}</p>
          **</div>
        **</article>
    **{% endfor %}
    **{% if is_paginated %}

      **{% if page_obj.has_previous %}
        **<a class="btn btn-outline-info mb-4" href="?page=1">First</a>
        **<a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
      **{% endif %}

      **{% for num in page_obj.paginator.page_range %}
        **{% if page_obj.number == num %}
          **<a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
        **{% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
          **<a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
        **{% endif %}
      **{% endfor %}

      **{% if page_obj.has_next %}
        **<a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
        **<a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
      **{% endif %}

    **{% endif %} 
**{% endblock content %}
