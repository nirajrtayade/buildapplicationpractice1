
from djongo import models
from bson import ObjectId

def generate_objectid():
    return str(ObjectId())


class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_objectid)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_objectid)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_objectid)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()
    def __str__(self):
        return f"{self.user.name} - {self.type} on {self.date}"


class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_objectid)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(Team, blank=True)
    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False, default=generate_objectid)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.team.name} - {self.points} pts"
