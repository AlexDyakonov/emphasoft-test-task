from django.urls import include, path, re_path

from .views import CustomAuthToken, UserDetailView, UserListView

urlpatterns = [
    path("auth/token/", CustomAuthToken.as_view()),
    path("users/", UserListView.as_view(), name="users-list"),
    path("users/<str:username>/", UserDetailView.as_view(), name="customuser-detail"),
]
