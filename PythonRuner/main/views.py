from django.http import HttpResponse
from codeRuner import accept_user_input


def index(request):

    #accept_user_input(name, code, par=[], values=[])
    return HttpResponse("Hello, world. You're at the polls index.")