from django.shortcuts import render
from .models import School
from .forms import SchoolAddForm, CommentForm
from django.views.generic import ListView, TemplateView
from django.shortcuts import render, get_object_or_404

class HomePageView(TemplateView):
    template_name = 'home.html'


class SchoolListView(ListView):
    model = School
    template_name = 'listschool.html'
    context_object_name = 'schools'

class SchoolAddViews(TemplateView):
    template_name = 'addschool.html'
    
    def get(self, request):
        form = SchoolAddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SchoolAddForm(request.POST)

        if form.is_valid():
            name  = form.cleaned_data['name']
            description = form.cleaned_data['description']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            public = form.cleaned_data['public']
            students = form.cleaned_data['students']
            rating = form.cleaned_data['rating']


            new_school = School(name = name, description = description, address = address, city = city, latitude = latitude, longitude = longitude, public = public, students = students, rating = rating)
            new_school.save()

        else:
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})

class SchoolDetailView(TemplateView):
    template_name = 'schooldetail.html'
    id = None

    def get(self, request, id):
        school = School.objects.get(id=id)
        comments = school.comments.filter(active=True)
        new_comment = None
        comment_form = CommentForm(data=request.POST)
        if request.method == 'POST':
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
            else:
                comment_form = CommentForm()
        return render(request, self.template_name, {'school':school, 'comments': comments, 'new_comment': new_comment,'comment_form': comment_form})
