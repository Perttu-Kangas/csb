from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    id = request.GET.get('id')
    content = Message.objects.get(pk=id).content
    return HttpResponse(content)
