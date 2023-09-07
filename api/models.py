# from django.db import models

# class EndpointData(models.Model):
#     """Represent a endpoint data.
    
#     Attributes:
#         slack_name: The user slack name.
#         current_day: The current date.
#         utc_timeutc_time: The current time.
#         track: The user HNGx track.
#         github_file_url: The user github file url.
#         github_repo_url: The user github repo url.
#     """
#     slack_name = models.CharField(max_length=255, null=True)
#     current_day = models.CharField(max_length=20)
#     utc_time = models.DateTimeField()
#     track = models.CharField(max_length=20, null=True)
#     github_file_url = models.URLField()
#     github_repo_url = models.URLField()
