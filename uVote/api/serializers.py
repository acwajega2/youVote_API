from rest_framework import serializers



from uVote.models import Election_Race, Candidate,Voting_register



#Serializer for the users



#---Election Race Serializer
class ElectionRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election_Race
      
        fields = '__all__'


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
       
        fields = '__all__'
    
class Voting_registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting_register
        
        fields = '__all__'
    