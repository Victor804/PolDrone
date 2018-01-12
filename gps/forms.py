from django import forms 
from models import ProcessingNode, Project

class ProcessingNodeForm(forms.ModelForm):
    class Meta:
        model = ProcessingNode
        fields = "__all__" 
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"