from django import forms 
from models import Flight, Project

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__" 
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"