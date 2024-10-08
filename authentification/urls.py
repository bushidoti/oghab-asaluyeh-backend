from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.OfficeView.as_view(), name='home'),
    path('name/', views.FullNameView.as_view(), name='name'),
    path('date/', views.DateView.as_view(), name='name'),
    path('permission/', views.PermissionView.as_view(), name='permission'),
    path('permission_detailed/', views.PermissionComplexView.as_view(), name='permission_detailed'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
