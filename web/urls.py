from django.urls                import path
from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('blog/', views.blog_list, name='blog_list'),  # Blog listing page
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),  # Blog details page
    path('search/', views.search, name='search'),  # Search functionality
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

