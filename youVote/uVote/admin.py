from django.contrib import admin
from .models import Election_Race,Candidate,Voting_register

# Register your models here.

admin.site.register(Election_Race)
admin.site.register(Candidate)
admin.site.register(Voting_register)