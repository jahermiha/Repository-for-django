from typing import Any, Dict
from django import forms
from django.core import validators


class contactForm(forms.Form):
    name=forms.CharField(label="User Name",help_text="total length must be within 70 characters,",
    required = False,widget=forms.TextInput(attrs={'Placeholder':'Enter your Name'}),
    validators=[validators.MinLengthValidator(10,message='enter the minmun 10 characters ')])
    
    
    email=forms.EmailField(label="User Email",widget=forms.EmailInput,validators=[validators.EmailValidator])
    
    
    comment=forms.CharField(widget = forms.Textarea(attrs={'Placeholder':'Enter your Comment'}))
    
    
    
    age = forms.IntegerField(validators=[validators.MaxValueValidator(30, message="age must be maximum 34"),
    validators.MinValueValidator(18, message="age must be at least 24")])

    
    FILES=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'],
    message = 'File Extension must be ended with .pdf')])
    

    
    
    # weight= forms.FloatField()
    # balance =forms.DecimalField()
    # check=forms.BooleanField()
    
    
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    
    
    MEAL=[('S','Small'),('M','Mashroom'),('B','beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
    
    
    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
 
           
    
    # def clean(self): 
    #    cleaned_data= super().clean()
    #    valname=self.cleaned_data['name']
    #    valemail=self.cleaned_data['email']
    #    if len(valname)<10:
    #        raise forms.ValidationError('enter a name at last 10 characters')
    #    if '.com' not in valemail:
    #        raise forms.ValidationError('your email must contain .com')
           
    
    
    
     