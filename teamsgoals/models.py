from django.db import models


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=False)
    city = models.CharField(max_length=250, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=False)
    goals = models.IntegerField(blank=True, null=False)
    team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
