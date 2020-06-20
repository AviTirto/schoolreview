from django import forms
from schoolapp.models import School, Comment

class SchoolAddForm(forms.Form):
    name = forms.CharField(max_length = 50)
    description = forms.CharField(max_length = 500, widget=forms.Textarea)
    address = forms.CharField(max_length = 100, widget=forms.Textarea)
    city = forms.CharField(max_length = 50)
    latitude = forms.DecimalField(decimal_places = 3, max_digits = 5)
    longitude = forms.DecimalField(decimal_places = 3, max_digits = 5)
    public = forms.BooleanField()
    students = forms.IntegerField()
    rating = forms.DecimalField(decimal_places = 3, max_digits = 5)
    image = forms.ImageField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'content', 'rating')