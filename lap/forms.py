# import form class from django
from django import forms

from .models import Laptop , repair
from .models import kpi

# create a ModelForm
class AddLaptop(forms.ModelForm):
	# specify the name of model to use
    class Meta:
        
        #bring the kpi strings for dropdown
        age_qry = kpi.objects.filter(type='Laptop_age').values()
        AGE_CHOICES = []
        for option in age_qry:
            x = (option['match_string'] , option['match_string'] )
            AGE_CHOICES.append(x)
            
            
        motherboard_qry = kpi.objects.filter(type='Motherboard').values()
        MOTHER_CHOICES = []
        for option in motherboard_qry:
            x = (option['match_string'] , option['match_string'] )
            MOTHER_CHOICES.append(x)
            
        display_qry = kpi.objects.filter(type='Display').values()
        DISPLAY_CHOICES = []
        for option in display_qry:
            x = (option['match_string'] , option['match_string'] )
            DISPLAY_CHOICES.append(x)
            
        processor_qry = kpi.objects.filter(type='Processor').values()
        PROCESSOR_CHOICES = []
        for option in processor_qry:
            x = (option['match_string'] , option['match_string'] )
            PROCESSOR_CHOICES.append(x) 
            
            
        speed_qry = kpi.objects.filter(type='Speed').values()
        SPEED_CHOICES = []
        for option in speed_qry:
            x = (option['match_string'] , option['match_string'] )
            SPEED_CHOICES.append(x)
        #temp drop = 'motherboard_condition': forms.Select(choices=MOTHER_CHOICES)
    
        model = Laptop
        #fields = "__all__"
        fields = ('name', 'sap_id', 'phone', 'laptop_brand', 'laptop_serial', 'laptop_age', 'motherboard_condition','display_condition','processor_age','speed','report_date')
        widgets = {'report_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}) , 'laptop_age': forms.Select(choices=AGE_CHOICES),'motherboard_condition': forms.Select(choices=MOTHER_CHOICES),'display_condition': forms.Select(choices=DISPLAY_CHOICES),'processor_age': forms.Select(choices=PROCESSOR_CHOICES),'speed': forms.Select(choices=SPEED_CHOICES)}
      
       
        
class Service_request(forms.ModelForm):
	# specify the name of model to use
    class Meta:
        OS_CHOICES = [('Windows 11', 'Windows 11'),('Windows 10', 'Windows 10'),('macOS', 'macOS'),]
        Brand_CHOICES = [('Lenovo', 'Lenovo'),('Dell', 'Dell'),('HP', 'HP'),('Apple','Apple'),('Others','Others')]
        Urgency_CHOICES = [('Normal', 'Normal'),('Urgent','Urgent'),('Very Urgent', 'Very Urgent')]
        model = repair
        fields = "__all__" 
        widgets = {'report_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),'laptop_os': forms.Select(choices=OS_CHOICES),'laptop_brand': forms.Select(choices=Brand_CHOICES),'urgency': forms.Select(choices=Urgency_CHOICES)}
        
