
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web-scrap/api/', include('web_scrap.api.urls')),
    path('data-science/api/', include('data_science.api.urls')),




    path('__debug__/', include('debug_toolbar.urls')),
]
