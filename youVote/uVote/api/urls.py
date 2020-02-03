from django.urls import path, include

from .views import CandidateListAPIView,Election_RaceListAPIView,Voting_registerListAPIView


#------API AUTHORISATION


urlpatterns = [
    # For Api Authorisation
    



    path('candidates/', CandidateListAPIView.as_view()),
    path('election_race/', Election_RaceListAPIView.as_view()),
    path('voting_register/',Voting_registerListAPIView.as_view())
]
