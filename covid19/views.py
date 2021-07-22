from django.http import HttpResponse

def index(request):
    return HttpResponse("코로나19 대시보드")