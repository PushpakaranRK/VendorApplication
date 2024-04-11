from . import views
from django.urls import path
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

app_name = 'administrator'

urlpatterns = [

    path('dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('add_category', views.admin_add_category, name='admin_add_category'),
    path('review_product', views.admin_review_product, name='admin_review_product'),
    path('view_product', views.admin_view_product, name='admin_view_product'),
    path('view_category', views.admin_view_category, name='admin_view_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
