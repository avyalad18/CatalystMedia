from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class AuthUser(AbstractUser):
    username = models.CharField( max_length=255, unique=True, db_column='username', null=False)
    password = models.CharField( max_length=255, db_column='password', null=False)
    email = models.CharField(max_length=255, unique=True,db_column='email', null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, db_column='first_name')
    last_name = models.CharField(max_length=150, blank=True, null=True, db_column='last_name')
    date_joined = models.DateTimeField(auto_created=True, null=True, db_column='date_joined')
    is_active = models.BooleanField(default=True, db_column='is_active')
    is_superuser = models.BooleanField(default=False, db_column='is_superuser')
    is_staff = models.BooleanField(default=True, db_column='is_staff')

    USERNAME_FIELD = 'username'

    class Meta:
        managed = True
        db_table = "auth_user"


    def save(self, *args, **kwargs):       
        if not self.password.startswith('pbkdf'):
            self.password = make_password(self.password)
        super(AuthUser, self).save(*args, **kwargs)
        
    
