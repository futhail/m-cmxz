from django import forms

from .models import Branches,Transfers,Transfers_dsactvita









class New_Branche(forms.ModelForm):
    # conservative = forms.CheckboxSelectMultiple(attrs={'placeholder':'Choic conservative'},choices=('sanaa','adan','almhout'))
    
    class Meta:
        model = Branches
        fields = ['branche_id','conservative','name_branche','directorated']

class New_Transfers(forms.ModelForm):

    class Meta:
        model = Transfers
        fields = ['name_send','phon_send','amount','courrency','name_recipient','phon_recipient','recipient_card_type']




class form_card_recipient(forms.Form):
    pk=forms.IntegerField()


class form_card_recipient_2(forms.ModelForm):
    class Meta:
        model= Transfers_dsactvita
        fields = ['recipient_card_num_d']

# class New_Signup(forms.ModelForm):
#     # email = forms.CharField(max_length=250, required=True,
#     #  widget=forms.EmailInput())
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput())

#     class Meta:
#         model = Sign_up
#         fields = ['user_name','password','phon','conservative_user','directorated_user','branche_id_for']



# class BlogCreateView(CreateView): # new 
#     model = Post template_name = 'post_new.html' fields = ['title', 'author', 'body']