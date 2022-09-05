from django.db import models

# Create your models here.


class Education(models.Model):
    major = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    comments = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-end_date']

    def __str__(self):
        return "{} at {}".format(self.major, self.institution)


class Subject(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    weight = models.DecimalField(decimal_places=3, max_digits=4, default=0)

    class Meta:
        ordering = ['education', '-weight']

    def __str__(self):
        return self.name


class Experience(models.Model):
    organization = models.CharField(max_length=50)
    job_title = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    class Meta:
        ordering = ['-end_date']

    def __str__(self):
        return "{} at {}".format(self.job_title, self.organization)


class Location(models.Model):
    experience = models.ForeignKey(
        Experience, null=True, on_delete=models.CASCADE)
    education = models.ForeignKey(
        Education, null=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

    def __str__(self):
        return "{}, {}".format(self.city, self.country)
