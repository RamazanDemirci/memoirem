from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def memories(request):
    if request.method == 'GET':
        pass
