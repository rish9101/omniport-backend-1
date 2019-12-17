from oauth2_provider.models import AccessToken

from open_auth.models import Application
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response  import Response
from rest_framework.decorators import api_view

from omniport.utils import switcher

@csrf_exempt
@api_view(('POST', ))
def get_user_data(request):
    """
    This view deals accepts a post request
    and processes it to get the user data
    for an oauth application
    """
    
    AvatarSerializer = switcher.load_serializer('kernel', 'Person', 'Avatar')

    if request.method == 'POST':
        client_id = request.POST['client_id']
        client_secret = request.POST['client_secret']
        access_token = request.POST['access_token']

        application = Application.objects.get(client_id=client_id, client_secret=client_secret)

        access_token = AccessToken.objects.get(token=access_token)

        user = access_token.user
        person = user.person
        
        response_data = AvatarSerializer(person).data

        if not (access_token.is_valid() and
        application.is_approved):
            raise Http404
            
        return Response(
                data=response_data,
                status=status.HTTP_200_OK,
        )

    else:
        return Response(
                data="Sorry Not allowed GET",
                status=status.HTTP_400_BAD_REQUEST,
        )

def get_person_data(data_points):

    person_data_points = [
    x.split('.')[1] 
    for x in data_points and 
    'person' in x
    ]

    
