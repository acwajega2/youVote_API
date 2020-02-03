from django.db import models
from django.db.models import F
from django.db.models import Max  # for getting the maximum number


# Create your models here.


# Elections Model
class Election_Race(models.Model):
    status = ( ('Y','Yes'),('N','No')
        
    )
       
       
    election_name = models.CharField(max_length=150)
    election_status = models.CharField(max_length=50, choices=status)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.election_name
    



#Creating the Candidates model
class Candidate(models.Model):
    name = models.CharField(max_length=120)
    profile_pic = models.CharField(max_length=400)
    election_race = models.ForeignKey(Election_Race,on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
   
   

    class Meta:
        verbose_name_plural = "Candidates"

    #property to show if the candidate is leading the race
    @property
    def is_leading(self):
        if self.vote_count == 0:
            return False
        else:
            if self.vote_count == Candidate.objects.aggregate(Max('vote_count')):
                return True
            else:
                return False

            
        
    def __str__(self):
        return self.name



#Voting Model
class Voting_register(models.Model):
    status = ( ('Y','Yes'),('N','No')
        
    )
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vote = models.CharField(max_length=20, choices=status)
    created = models.DateTimeField(auto_now_add=True)
    
    
   
   # Updating the votes a cadidate has gotten as you save
    def save(self, *args, **kwargs):
       if not self.pk:
           if self.vote == "Y":
               Candidate.objects.filter(pk=self.candidate_id).update(vote_count=F('vote_count') + 1)
       super().save(*args, **kwargs) 
               

           
           
    
        
    


    
    