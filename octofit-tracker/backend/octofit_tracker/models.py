from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.EmbeddedField(model_container=User)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.EmbeddedField(model_container=User)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
