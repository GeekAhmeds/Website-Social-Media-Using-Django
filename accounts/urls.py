from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

path('', views.home),
path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
path('register/', views.register, name="register"),
path('profile/', views.view_profile, name="view_profile"),
path('profile/edit/', views.edit_profile, name="edit_profile"),
path('change-password/', views.change_password, name="change_password"),
path('password_reset/', PasswordResetView.as_view(template_name='accounts/reset_password.html') ,name="password_reset"),
path('password_reset_done/', PasswordResetDoneView.as_view() ,name="password_reset_done"),
path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view() ,name="password_reset_confirm"),
path('password_reset_complete', PasswordResetCompleteView.as_view() ,name="password_reset_complete"),

]
