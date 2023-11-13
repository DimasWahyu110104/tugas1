from django.db import models

class Biodata(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Contak(models.Model):
  Nama = models.CharField(max_length=255)
  No_Hp = models.IntegerField()
  Email = models.CharField(max_length=255)

  def __str__(self):
    return f" {self.Nama} {self.No_Hp} {self.Email}"