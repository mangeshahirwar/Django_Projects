"""
URL configuration for catalyst_count project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from file_upload_app import views  # Import the 'views' module from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file_upload_app/', include('file_upload_app.urls')), 
    path('api/', include('file_upload_app.urls')),  # Include the app's URLs under the '/api/' path

    #path('file_upload_app/', include('api.urls')), 
    #path('file_upload_app/', include('api.urls')), 



]
