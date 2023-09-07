from django.http import JsonResponse
import datetime
import json
from django.utils import timezone

def list(request):
    # the get query from url
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    # Get the current UTC time
    current_utc_time = timezone.now()

    # Validate input
    if not slack_name or not track:
        return JsonResponse({"error":"Both slack name and track must be provided"}, status=400)
    
    github_repo = "https://github.com/johndiginee/Backend_Stage_One_Task_Main"
    github_file = "https://github.com/johndiginee/Backend_Stage_One_Task_Main/blob/master/api/views.py"
    cur_day = datetime.datetime.utcnow().strftime('%A')
    utctime = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')


    response_data = { 
        "slack_name": slack_name,
        "current_day": cur_day,
        "utc_time": utctime,
        "track": track,
        "github_file_url": github_file,
        "github_repo_url": github_repo,
        "status_code": 200
    }
    return JsonResponse(response_data)