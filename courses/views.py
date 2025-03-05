from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Course
from .forms import CourseSearchForm

def search_courses(request):
    form = CourseSearchForm(request.GET or None)
    courses = None

    if form.is_valid():
        query = form.cleaned_data.get("query")
        courses = Course.objects.filter(name__icontains=query)  # ค้นหาจากชื่อวิชา

    return render(request, "courses/search.html", {"form": form, "courses": courses})
