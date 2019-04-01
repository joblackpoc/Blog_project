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
 - Paginator -> user_posts.html
<br/>
     {% if is_paginated %}
<br/>
       {% if page_obj.has_previous %}
         <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
         <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
       {% endif %}
<br/>
       {% for num in page_obj.paginator.page_range %}
         {% if page_obj.number == num %}
           <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
         {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
           <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
         {% endif %}
       {% endfor %}
<br/>
       {% if page_obj.has_next %}
         <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
         <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
       {% endif %}
<br/>
     {% endif %}

