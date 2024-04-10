from django.db import models
from django.contrib.auth.models import User


class Availability(models.Model):
    availabilityID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.startTime} to {self.endTime}"

    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = 'Availability'


class Projects(models.Model):
    projectID = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100)

    def __str__(self):
        return self.projectName

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

class Activities(models.Model):
    activityID = models.AutoField(primary_key=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    activityName = models.CharField(max_length=100)

    def __str__(self):
        return self.activityName
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activity'

class Translations(models.Model):
    translationID = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    textVolume = models.IntegerField()
    completionPercentage = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.activity.activityName}"
    class Meta:
        verbose_name = 'Translation'
        verbose_name_plural = 'Translation'

class Checks(models.Model):
    checkID = models.AutoField(primary_key=True)
    translation = models.ForeignKey(Translations, on_delete=models.CASCADE)
    checkResult = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.translation.user.username} - {self.checkResult}"
    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Check'

class Mistakes(models.Model):
    mistakeID = models.AutoField(primary_key=True)
    translation = models.ForeignKey(Translations, on_delete=models.CASCADE)
    mistakeDescription = models.TextField()

    def __str__(self):
        return f"{self.translation.user.username} - {self.mistakeDescription}"
    class Meta:
        verbose_name = 'Mistake'
        verbose_name_plural = 'Mistake'

class Replacement(models.Model):
    replacementID = models.AutoField(primary_key=True)
    translation = models.ForeignKey(Translations, on_delete=models.CASCADE)
    replacementDate = models.DateField()

    def __str__(self):
        return f"{self.translation.user.username} - {self.replacementDate}"
    class Meta:
        verbose_name = 'Replacement'
        verbose_name_plural = 'Replacement'