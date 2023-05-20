from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request, user_pk):
    

@api_view(['POST', 'PUT'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        nickname = request.data.get('nickname')
        email = request.data.get('email')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        profile_img = request.data.get('profile_img')
        if profile_img == None:
            profile_img = 'null'

        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({'이미 가입된 아이디 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({'이미 가입된 이메일 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(nickname=request.data.get('nickname')).exists():
            return Response({'이미 존재하는 닉네임 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        currentuser = request.data.get('currentuser')
        id = User.objects.get(username=currentuser).id
        currentpw = request.data.get('currentpw')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        nickname = request.data.get('nickname')
        email = request.data.get('email')
        profile_img = request.data.get('profile_img')
        if profile_img == None:
            profile_img = 'null'

        user = get_object_or_404(User, pk=id)
        print(1)
        if user.check_password(currentpw):
            print(2)
            if password != password_confirmation:
                return Response({'error': '비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=request.data.get('email')).exists() and email != user.email:
                return Response({'error': '이미 가입된 이메일 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(nickname=request.data.get('nickname')).exists() and nickname != user.nickname:
                return Response({'error': '이미 존재하는 닉네임 입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
            user.nickname = nickname
            user.profile_img = profile_img
            user.email = email
            user.set_password(request.data.get('password'))
            user.save()

            return Response(status=status.HTTP_200_OK)
        
        else:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            