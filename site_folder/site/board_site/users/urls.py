from django.urls import path
from . import views
from users.api.urls import api_users_urlpatterns


# app_name="users"

users_urlpatterns = [
    path('accounts/register/', views.RegisterUser.as_view(), name="register"),
    path('accounts/logout/', views.logout_user, name="log_out"),
    path('accounts/login/', views.LoginUser.as_view(), name="login"),
    path('accounts/users/profile/<int:pk>/', views.UserProfile.as_view(), name="profile"),
    path('accounts/users/change_password/', views.AUserPasswordChange.as_view(), name="change_password"),
    path('accounts/users/change_password/done/', views.password_change_done, name="password_done"),
    
    path('accoutnts/user/items/', views.user_products, name="user_created_products")
    # path('accounts/password_change/', UserPasswordChange.as_view(), name='password_change'),

]

