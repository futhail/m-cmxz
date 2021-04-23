from django.db import models

from django.contrib.auth.models import User






YEAR_IN_SCHOOL_CHOICES = [
    ('صنعاء','صنعاء'),
    ('صعده ','صعده '),
    ('المحويت','المحويت'),
    ('عمران','عمران '),
    ('ذمار','ذمار '),
    ('مارب','مارب'),
    ('عدن','عدن'),

]
class Branches(models.Model):  
    branche_id = models.IntegerField(primary_key=True,unique=True)
    name_branche =models.CharField(max_length=100)
    conservative = models.CharField(max_length=30,choices=YEAR_IN_SCHOOL_CHOICES)
    directorated = models.CharField(max_length=30)
    date_created = models.DateField(auto_now=True)


    def __str__(self):
        return self.branche_id

courr=[
    ('ريال يمني','ريال يمني'),
    ('دولار','دولار'),
    ('يورو','يورو'),
    ('ريال سعودي','ريال سعودي'),
]

ss=[(str(i.branche_id),i.name_branche) for i in Branches.objects.all()]
class Transfers(models.Model):
    id_transfer = models.IntegerField(primary_key=True,unique=True)
    name_send = models.CharField(max_length=200,help_text='plase enter name sender')
    phon_send = models.IntegerField()
    amount = models.IntegerField()
    courrency = models.CharField(max_length=30,choices=ss)
    date_send = models.DateTimeField(auto_now=True)
    name_recipient = models.CharField(max_length=200)
    phon_recipient = models.IntegerField()
    situation = models.BooleanField(default=True) 
    recipient_card_type = models.CharField(max_length=50)
    id_user_sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')





 


#d= doen 

class Transfers_dsactvita(models.Model):
    id_transfer_d = models.IntegerField(primary_key=True)
    name_send_d = models.CharField(max_length=200,help_text='plase enter name sender')
    phon_send_d = models.IntegerField()
    amount_d = models.IntegerField()
    courrency_d = models.CharField(max_length=30)
    date_send_d = models.DateTimeField(auto_now=True)
    name_recipient_d = models.CharField(max_length=200)
    phon_recipient_d = models.IntegerField()
    situation_d = models.BooleanField(default=False)
    recipient_card_num_d = models.IntegerField()
    recipient_card_type_d = models.CharField(max_length=50)
    date_receipt_d = models.DateField(auto_now=True)
    id_user_sender_d = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_d')
    id_user_receipt_d = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='receipt')



# Create your models here.
