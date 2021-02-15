from django.contrib import admin
from django.urls import path, include

admin.site.site_header="Blogsite Admin"
admin.site.site_title="Blogsite "
admin.site.index_title="Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),

]
