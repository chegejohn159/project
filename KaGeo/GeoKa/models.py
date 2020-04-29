from django.db import models
#from encrypted_model_fields.fields import EncryptedCharField
#from django_cryptography.fields import encrypt
from fernet_fields import EncryptedCharField
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager

class usermanager(BaseUserManager):
	def create_user(self,email,password,firstname):
		user=self.model(email=email,password=password,firstname=firstname)
		user.set_password(password)
		user.is_staff=False
		user.is_superuser=False
		user.save(using=self._db)
		return user
	def create_superuser(self,email,password,firstname):
		user=self.create_user(email=email,password=password,firstname=firstname)
		user.is_active=True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user

class user(AbstractBaseUser,PermissionsMixin):
	password=EncryptedCharField(max_length=100)
	email=models.EmailField(unique=True)
	firstname=models.CharField(max_length=30,default="kamau")
	middlename=models.CharField(max_length=30,null=True)
	lastname=models.CharField(max_length=30,default="kamau")
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	is_doctor=models.BooleanField(default=False)
	is_patient=models.BooleanField(default=False)
	is_ceo=models.BooleanField(default=False)
	REQUIRED_FIELDS=['firstname']
	USERNAME_FIELD='email'

	objects=usermanager()

	def __str__(self):
		return self.email
	def get_short_name(self):
		return self.email
 

class MainCharacter(models.Model):
	name = models.CharField(max_length=128, unique=True)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
class Movie(models.Model):
	maincharacter = models.ForeignKey(MainCharacter, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	writer=models.ManyToManyField(user)
	url = models.URLField()
	views = models.IntegerField(default=0)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
                  

