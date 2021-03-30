from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from . import views
import sys
sys.path.append('..')
from accounts.views import RegisterView, guest_register_view, login_page, LoginView

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^create_delivery_contract/$', views.create_delivery_contract, name='create_delivery_contract'),
    path('table/<contract_id>/', views.table, name='table'),

    # Контракт
    path('create', views.create_delivery_contract, name='create'),
    path('update_contract/<pk>/', views.update_contract, name='update_contract'),
    path('delete_contract/<pk>/', views.delete_contract, name='delete_contract'),

    # Сроки
    path('create_timing/<kek>/', views.create_timing, name='create_timing'),
    path('update_timing/<kek>/', views.update_timing, name='update_timing'),
    path('delete_timing/<kek>/', views.delete_timing, name='delete_timing'),

    # Претензии
    path('penalty_to_us', views.penalty_to_us, name='penalty_to_us'),
    path('docs_upload', views.upload_doc, name='upload_doc'),
    path('penalty_to_another_side_reaction/<pk>/', views.penalty_to_another_side_reaction,
         name='penalty_to_another_side_reaction'),
    path('penalty_to_another_side_quality/<pk>/', views.penalty_to_another_side_quality,
         name='penalty_to_another_side_quality'),
    path('penalty_to_another_side_pay/<pk>/', views.penalty_to_another_side_pay,
         name='penalty_to_another_side_pay'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
