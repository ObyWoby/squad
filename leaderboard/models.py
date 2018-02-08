from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone




class LadderUser(User):
    profile_pic = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.username


class Team_12v12(models.Model):
    team_name = models.CharField(max_length=100)
    date_founded = models.DateTimeField(default=timezone.now)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.FileField()
    bio = models.TextField(max_length=500)
    elo = models.FloatField(default=1000)
    #team_admins = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse_lazy('leaderboard:detail-12v12', kwargs={'team12v12_id': self.pk})

    def __str__(self):
        return self.team_name

# To make the roster 12v12
class TeamMembership(models.Model):
    user = models.OneToOneField(LadderUser, related_name='team_membership', on_delete=models.CASCADE)
    team = models.OneToOneField(Team_12v12, related_name='roster', on_delete=models.CASCADE)

# To show planned matches, scoreboard, and match history of each team 12v12
#class Match(models.Model):
    #teama = models.ForeignKey(Team_12v12, on_delete=models.CASCADE)
    #teamb = models.ForeignKey(Team_12v12, on_delete=models.CASCADE)
    #match_date = models.DateTimeField()
    #created_at = models.DateField(auto_now_add=True)
    #modified_at = models.DateField(auto_now=True)




#Alex's

#some decisions to make here, do we just want to record after a match? or create a model for an upcomin match, and fill in results when done?
#class Match(models.Model):
    ###teama = models.OneToOneField(Team, related_name='matches')
    ###teamb = models.OneToOneField(Team, related_name='matches_alt')
    ###cancalled two lines above, would be hard to query and list - may make sense if you always have a "challenger" or something
    ###I am using another "connection" model below instead (MatchParticipation)
    ###buut, this may be a good time to use a "many-x" connection - I generally prefer a "connection" model though, as extra data can be stored on the connection

    #planned_date = models.DateField()#could perhaps be a datetimefield

    #winner = models.OneToOneField(Team, related_name='won_matches', null=True, blank=True)
    ###could also fill in a loser

    #created_at = models.DateField(auto_now_add=True)
    #modified_at = models.DateField(auto_now=True)

#class MatchParticipation(models.Model):
    #match = models.OneToOneField(Match, related_name='teams')
    #team = models.OneToOneField(Team, related_name='matches')
    #created_at = models.DateField(auto_now_add=True)
    #modified_at = models.DateField(auto_now=True)