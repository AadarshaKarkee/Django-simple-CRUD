from django.forms import ModelForm
from .models import News

class NewsAddForm(ModelForm):
    
    class Meta:
        model = News
        fields = ("title","slug", "category", "body")
