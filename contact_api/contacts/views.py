from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Contact, UserCredentials
from .serializers import ContactSerializer
from django.contrib.auth.hashers import check_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed, JsonResponse

class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

@csrf_exempt
def verify_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'JSON malformado', 'details': str(e)}, status=400)

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Faltan datos'}, status=400)

        try:
            user = UserCredentials.objects.get(username=username)
        except UserCredentials.DoesNotExist:
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)

        if check_password(password, user.password):
            return JsonResponse({'message': 'Usuario y contraseña válidos'})
        else:
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)
    else:
        return HttpResponseNotAllowed(['POST'])