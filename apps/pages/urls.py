from django.urls import path

from apps.pages.views import home_page_view, blog_page_view

app_name = 'pages'

urlpatterns = [
    path('blog/',blog_page_view, name='blogs'),
    path('',home_page_view, name='home'),
]