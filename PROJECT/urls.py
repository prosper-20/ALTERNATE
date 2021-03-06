"""PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostCreateView
from users.views import register, login, profile
from content.views import about, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('content.urls')),
    path("blog/", include("blog.urls")),
    path("post/new/", PostCreateView.as_view(), name="post_create" ),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path('profile/', profile, name="profile"),
    path("about-us/", about, name="about"),
    path("gallery/", gallery, name="gallery")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Alternate Media'

admin.site.index_title = 'Alternate Media'                 # default: "Site administration"
admin.site.site_title = 'Admin' # default: "Django site admin"
