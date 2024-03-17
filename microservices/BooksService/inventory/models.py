from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20,null=False)
    authors = models.CharField(max_length=20,null=False)
    isbn = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)

    class Meta :
        managed = True
        db_table='Books'

