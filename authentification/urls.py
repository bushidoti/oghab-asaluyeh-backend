from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.OfficeView.as_view(), name='home'),
    path('name/', views.FullNameView.as_view(), name='name'),
    path('permission/', views.PermissionView.as_view(), name='permission'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
