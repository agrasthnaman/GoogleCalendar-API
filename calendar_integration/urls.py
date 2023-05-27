from django.urls import path
from calendar_integration.views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view()),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view()),
]
