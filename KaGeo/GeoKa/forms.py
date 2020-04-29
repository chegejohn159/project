# from django import forms

# class form1(forms.Form):
# 	post=forms.CharField()


from django import forms
from fernet_fields import EncryptedCharField
from .models import user,Movie,MainCharacter
class form1(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	middlename=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30,'placeholder':'Type your password'}))
	
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Email Address'}))
	class Meta:
		model = user
		fields = ('firstname','middlename','lastname', 'email','password',)

class movie1(forms.ModelForm):
	maincharacter = forms.ModelChoiceField(queryset=MainCharacter.objects.all(),initial='')
	writer = forms.ModelMultipleChoiceField(queryset=user.objects.all(),initial='')
	#title = forms.ModelChoiceField(queryset=Movie.objects.all(),initial='')


	class Meta:
		model = Movie
		fields = ('maincharacter', 'title','writer','url','views',)
class char1(forms.ModelForm):
	
	class Meta:
		model = MainCharacter
		fields = ('name',)