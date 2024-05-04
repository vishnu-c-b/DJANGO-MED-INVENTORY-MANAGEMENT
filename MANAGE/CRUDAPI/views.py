from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .forms import CreateUserForm,LoginForm,Create,Update,Search
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Medicine
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
# Create your views here.
def HOMEPAGE(request):
    return render(request, 'HOME.html')


@api_view(['POST'])
@permission_classes((AllowAny,))    
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(data=request.data)

        if form.is_valid():

            form.save()

            return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))  
def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},
                                status=HTTP_400_BAD_REQUEST)
            user = authenticate(request, username=username, password=password)

            if not user:
              return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")
    return Response("Logout success!", status=status.HTTP_201_CREATED)
    




@login_required(login_url='log')
def inner(request):
     records = Medicine.objects.all()
   
     return render(request, 'INNER.html',{'record': records})




@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create(request):
    form=Create()
    if request.method == "POST":

        form = Create(request.POST)

        if form.is_valid():

            p=form.save()

            return Response({'id': p.m_id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @login_required(login_url='log')
def list(request):
    products = Medicine.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)







@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    product = get_object_or_404(Medicine,pk=pk)
    form = Update(request.data, instance=product)
    if form.is_valid():
        form.save()
       
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    try:
        product = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")







from django.shortcuts import HttpResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):

    query = request.GET.get('q')
    results = Medicine.objects.filter(mname__icontains=query)  
    serialized_results = [{'id': record.m_id, 'name': record.mname} for record in results]
    return JsonResponse({'results': serialized_results})
   
        
