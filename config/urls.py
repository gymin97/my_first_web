"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.view_blog_list),
    path('blog/view_blog/<int:blog_id>/', blog.views.view_blog),
    path('blog/add_blog_form/', blog.views.add_blog_form),
    path('blog/add_blog/', blog.views.add_blog),
    path('blog/edit_blog_form/<int:blog_id>/', blog.views.edit_blog_form),
    path('blog/edit_blog/', blog.views.edit_blog),
    path('blog/delete_blog/<int:blog_id>/', blog.views.delete_blog),
]
