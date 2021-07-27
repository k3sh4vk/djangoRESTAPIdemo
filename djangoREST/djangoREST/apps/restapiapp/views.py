from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import LoginForm
from .models import webUsers
from .serializers import webUsersSerializer
# Create your views here.


@api_view(['GET'])
def apiAccess(request):
    apiResponse = {
        'List Users': '/user-list/',
        'Detail View': '/user-details/<int:pk>/',
        'Create User': '/user-create/',
        'Update User': '/user-update/<int:pk>/',
        'Delete User': '/user-delete/<int:pk>/'
    }
    return Response(apiResponse)


@api_view(['GET'])
def userList(request):
    users = webUsers.objects.all()
    usersSerializer = webUsersSerializer(users, many=True)
    return Response(usersSerializer.data)


@api_view(['GET'])
def userDetail(request, pk):
    try:
        users = webUsers.objects.get(id=pk)
        usersSerializer = webUsersSerializer(users, many=False)
        return Response(usersSerializer.data)
    except:
        return Response({'message': 'UserDoesNotExist'})


@api_view(['GET', 'POST'])
def userCreate(request):
    if request.method == 'POST':
        usersSerializer = webUsersSerializer(data=request.data)
        if  usersSerializer.is_valid():
            usersSerializer.save()
        return Response(usersSerializer.data)
    else:
        infoResponse = {
            'username': 'VALUE',
            'email_id': 'VALUE'
        }
        return Response(infoResponse)


@api_view(['GET', 'POST'])
def userUpdate(request, pk):
    users, usersSerializer = None, None
    try:
        users = webUsers.objects.get(id=pk)
    except:
        return Response({'message': "UserDoesNotExist"}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'POST' and users is not None:
        usersSerializer = webUsersSerializer(instance=users, data=request.data)
        if  usersSerializer.is_valid():
            usersSerializer.save()
            return Response(usersSerializer.data)
    else:
        usersSerializer = webUsersSerializer(users, many=False)
        return Response(usersSerializer.data)


@api_view(['GET', 'DELETE'])
def userDelete(request, pk):
    usersSerializer, users = None, None
    try:
        users = webUsers.objects.get(id=pk)
        usersSerializer = webUsersSerializer(users, many=False)
    except:
        pass
    if request.method=='DELETE' and users is not None:
        users.delete()
        return Response(data=None)
    else:
        try:
            return Response(usersSerializer.data)
        except:
            return Response({'message': "UserDoesNotExist"})


def loginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/')
    return render(request, 'userRegister/register.html', {'form': form})
