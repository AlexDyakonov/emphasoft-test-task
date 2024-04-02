from django.urls import include, path, re_path

from .views import CustomAuthToken, UserDetailView, UserListView

urlpatterns = [
    path("auth/token/", CustomAuthToken.as_view(), name="token"),
    path("users/", UserListView.as_view(), name="users-list"),
    path("users/<str:username>/", UserDetailView.as_view(), name="user-detail"),
    path("rooms/", include("apps.reservation.urls")),
]
