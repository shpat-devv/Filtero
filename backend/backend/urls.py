from django.contrib import admin
from django.urls import path, include

import user.urls
#import image.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    #path('image/', include('image.urls')),
]
