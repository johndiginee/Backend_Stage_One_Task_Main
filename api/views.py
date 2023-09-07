from rest_framework import viewsets
from .models import EndpointData
from .serializers import EndpointDataSerializer
from django.http import JsonResponse
import datetime

class EndpointDataViewSet(viewsets.ViewSet):
    """
    The endpoint data view set
    """
    def list(self, request):
        slack_name = request.query_params.get('john_diginee')
        track = request.query_params.get('backend')

        # Get current day of the week
        current_day = datetime.datetime.now().strftime('%A')

        # Get current UTC time within a +/-2 minute window
        utc_time = datetime.datetime.utcnow()

        # Create or update the record in the database
        endpoint_data, created = EndpointData.objects.update_or_create(
            slack_name=slack_name,
            defaults={
                'current_day': current_day,
                'utc_time': utc_time,
                'track': track,
                'github_file_url': f'https://github.com/johndiginee/Backend_Stage_One_Task_Main/blob/master/information_required.ext',
                'github_repo_url': 'https://github.com/johndiginee/Backend_Stage_One_Task_Main',
            }
        )

        serializer = EndpointDataSerializer(endpoint_data)
        return JsonResponse(serializer.data)
