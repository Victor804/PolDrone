from django import forms 
from models import ProcessingNode

class ProcessingNodeForm(forms.ModelForm):
    
    class Meta:
        model = ProcessingNode
        fields = "__all__" 