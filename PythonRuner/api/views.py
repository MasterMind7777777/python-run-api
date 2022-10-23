from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.http import HttpResponse
from main.codeRuner import accept_user_input

@api_view(['Post', ])
@permission_classes([permissions.AllowAny])
def run_code(request):
    name = request.data["name"] 
    code_provided = request.data["code"]
    par = request.data["par"] 
    values = request.data["values"] 

    output = accept_user_input(name, code_provided, par, values)
    print(output)

    response = HttpResponse(str(output), 'Content-Type: text/plain')
  
    return response