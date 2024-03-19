from django.forms import ModelForm
from .models import Classroom

class ClassroomForm(ModelForm):
    class Meta: # using Meta database
        model = Classroom  
        fields = '__all__'
