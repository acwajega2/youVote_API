from rest_framework import generics, mixins
#importing the models
from uVote.models import Election_Race, Candidate, Voting_register

# importing the serialzer classes
from .serializers import ElectionRaceSerializer, CandidatesSerializer, Voting_registerSerializer

from django.db.models import Q


#List Candidates View
class CandidateListAPIView(generics.ListCreateAPIView):
    serializer_class = CandidatesSerializer
    lookup_field = 'pk'

    #overiding the query_Set
    def get_queryset(self):
      
        return Candidate.objects.all()
    
    
#List ElectionRace View
class Election_RaceListAPIView(generics.ListCreateAPIView):
    serializer_class = ElectionRaceSerializer
    lookup_field = 'pk'

    #overiding the query_Set
    def get_queryset(self):
      
        return Election_Race.objects.all()


#List Voting Registry View
class Voting_registerListAPIView(generics.ListCreateAPIView):
    serializer_class = Voting_registerSerializer
    lookup_field = 'pk'

    #overiding the query_Set
    def get_queryset(self):
      
        return Voting_register.objects.all()
