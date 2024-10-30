from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from api.serializers.profile_serializer import UserRegisterSerializer
# from rest_framework.permissions import IsAdminUser

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    # permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        # El get se encarga de buscar el serialezer_class
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        
        response_data = {
            "message": "Usuario registrado exitosamente",
            "user": UserRegisterSerializer(user).data
        }
        
        return Response(
            response_data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
