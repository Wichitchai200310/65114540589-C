from django import forms

class CourseSearchForm(forms.Form):
    query = forms.CharField(label="ค้นหาชื่อวิชา", max_length=200)
