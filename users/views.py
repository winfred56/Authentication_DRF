from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UsersListSerializer
from .models import UserManger
from rest_framework.generics import ListAPIView

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        register = RegisterSerializer(data=request.data)
        if register.is_valid():
            new_user = register.save()
            if new_user:
                return Response(register.data, status=status.HTTP_201_CREATED)
        return Response(register.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class UsersList(ListAPIView):
    queryset = UserManger.objects.all()
    serializer_class = UsersListSerializer

    def get_user_data(self, request):
        user = request.data

        if user.is_authenticated:
            return user.data
        return Response({'error': 'Anonymous User'}, status=status.HTTP_400_BAD_REQUEST)