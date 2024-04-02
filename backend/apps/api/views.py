from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .serializers import UserDetailSerializer, UserListSerializer

User = get_user_model()

# Так как я не создавал отдельного модуля для пользователей, поэтому сериализаторы и их логика тут прописана. По хорошему создать отдельный модуль
# и все это перенести туда.


class CustomAuthToken(ObtainAuthToken):
    """
    post:
    Аутентификация пользователя по 'username' и 'password'.

    Возвращает токен аутентификации и ID пользователя.
    """

    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "user_id": token.user_id})


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Получить или обновить информацию пользователя по 'username'.

    retrieve:
    Возвращает детальную информацию о пользователе.

    update:
    Обновляет информацию о пользователе. Требует аутентификации.
    """

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "username"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserListView(generics.ListCreateAPIView):
    """
    Список пользователей или создание нового пользователя.

    get:
    Возвращает список всех пользователей суперюзеру. Требует аутентификации.

    post:
    Создает нового пользователя. Доступно без аутентификации.
    """

    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == "POST" and self.request.user.is_superuser:
            return UserListSerializer
        return super().get_serializer_class()
