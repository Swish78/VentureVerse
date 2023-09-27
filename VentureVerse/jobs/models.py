from django.db import models
from django.contrib.auth.models import User

LOCATION_CHOICES = [
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Bengaluru', 'Bengaluru'),
    ('Hyderabad', 'Hyderabad'),
    ('Delhi', 'Delhi'),
    ('Indore', 'Indore'),
    ('Other', 'Other'),
]

SKILL_CHOICES = [
    ('Machine Learning', 'Machine Learning'),
    ('Blockchain', 'Blockchain'),
    ('Web Development', 'Web Development'),
    ('App Development', 'App Development'),
    ('DevOps', 'DevOps'),
    ('Full-time Academics', 'Full-time Academics'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Data Scientist', 'Data Scientist'),
]

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    skills = models.ManyToManyField(Skill, blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
