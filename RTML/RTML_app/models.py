from django.db import models

class ServiceModel(models.Model):

    ServName=models.CharField(max_length=60, primary_key=True)

    def __str__(self):
        return self.ServName


class TeamModel(models.Model):

    TeamName=models.CharField(max_length=60, primary_key=True)
    TeamServ=models.ForeignKey(ServiceModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.TeamName


class CommentModel(models.Model):

    CommTeam = models.ForeignKey(TeamModel, on_delete=models.PROTECT)
    CommText= models.TextField()

    def __str__ (self):
        return str(self.CommTeam) + " || " + str(self.CommText)
