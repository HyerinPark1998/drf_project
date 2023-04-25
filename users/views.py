from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializer import UserSerializers, UserProfileSerializers
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from users.models import User

# Create your views here.


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesage': '가입완료!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'mesage': f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user.is_admin = True
        user.saver()
        return Response('get 요청!')


class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        if request.user in you.followers.all():
            you.followers.remove(request.user)
            return Response('언팔로우하였습니다', status=status.HTTP_200_OK)
        else:
            you.followers.add(request.user)
            return Response('팔로우하였습니다', status=status.HTTP_200_OK)


class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializers(user)
        return Response(serializer.data)
