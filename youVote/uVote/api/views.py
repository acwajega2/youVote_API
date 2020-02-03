from rest_framework import generics, mixins
#importing the models
from uVote.models import Election_Race, Candidate, Voting_register

#PAgination
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

#for authentication
from rest_framework.permissions import IsAuthenticated

# importing the serialzer classes
from .serializers import ElectionRaceSerializer, CandidatesSerializer, Voting_registerSerializer

from django.db.models import Q

# PAgination
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    permission_classes = (IsAuthenticated,)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })

#List Candidates View
class CandidateListAPIView(generics.ListCreateAPIView):
    serializer_class = CandidatesSerializer
    lookup_field = 'pk'
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    #overiding the query_Set
    def get_queryset(self):
      
        return Candidate.objects.all()
    
    
#List ElectionRace View
class Election_RaceListAPIView(generics.ListCreateAPIView):
    serializer_class = ElectionRaceSerializer
    lookup_field = 'pk'
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    #overiding the query_Set
    def get_queryset(self):
      
        return Election_Race.objects.all()


#List Voting Registry View
class Voting_registerListAPIView(generics.ListCreateAPIView):
    serializer_class = Voting_registerSerializer
    lookup_field = 'pk'
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    #overiding the query_Set
    def get_queryset(self):
      
        return Voting_register.objects.all()
