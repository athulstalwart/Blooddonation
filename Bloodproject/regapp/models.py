from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Center(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    blood_group=models.CharField(max_length=124)
    phone=models.IntegerField()
    address=models.TextField(max_length=150)
    mailid=models.CharField(max_length=150,unique=True)

    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name