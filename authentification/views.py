from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from authentification.models import Employee


class FullNameView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': request.user.get_full_name()}
        return Response(content)


class OfficeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = Employee.objects.filter(user=request.user.id)
        content = {'message': result[0].office}
        return Response(content)


class PermissionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = Employee.objects.filter(user=request.user.id)
        content = {'message': result[0].rank}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
