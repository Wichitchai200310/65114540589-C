from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)  # รหัสวิชา
    name = models.CharField(max_length=200)  # ชื่อวิชา
    description = models.TextField(blank=True)  # คำอธิบาย
    credits = models.IntegerField()  # หน่วยกิต

    def __str__(self):
        return f"{self.code} - {self.name}"
