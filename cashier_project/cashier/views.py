from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,PermissionManager
from .form import New_Branche,New_Transfers,form_card_recipient,form_card_recipient_2
from .models import Branches , Transfers,Transfers_dsactvita
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.views.generic import UpdateView, ListView
   

import random





                                # Transfers_list_view
                    ######################################################
class TransferListView(ListView):
    model = Transfers
    context_object_name = 'transfers'
    template_name = 'table.html'
                    #########################################################

                            # Branches_list_view
                    ######################################################
class BranchesListView(ListView):
    model = Branches
    context_object_name = 'branche'
    template_name = 'tablebr.html'
                    #########################################################
                                            # new_branche
                    ##########################################################
@login_required
def new_branche(request):
    if request.method == 'POST':
        form_bar = New_Branche(request.POST)
        
        if form_bar.is_valid():
            form_bar.save()
            return redirect('new_branche')
    
    else:
        form_bar = New_Branche()
    return render(request,'manage.html',{ 'form_bar':form_bar })


                        ########################################################

class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}
class LoginView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'
    redirect_authenticated_user = False
    extra_context = None



def recipient(request):
    if request.method == 'POST':
        recipient=form_card_recipient(request.POST)
        if recipient.is_valid():
            quryii=Transfers.objects.all()
            qury=quryii.filter(id_transfer=recipient.cleaned_data['pk'])
            if qury.exists():
                return redirect('mana',pk=recipient.cleaned_data['pk'])
            else:
                return render(request,'resipientch.html',{'recipient':recipient,'recierror':'الحواله ليست موجوده'})
    else:
        recipient=form_card_recipient() 
    return render(request,'resipientch.html',{'recipient':recipient}) 

def my_tast(request,pk):
    qury=Transfers.objects.all()
    mana=qury.filter(id_transfer=pk)
    
    return render(request,'resipientcard.html',{'mana':mana})


def recipient_num_card(request,pk):
    if request.method == 'POST':
        form_card=form_card_recipient_2(request.POST)
        if form_card.is_valid():
            quryall=Transfers.objects.all()
            qury=quryall.filter(id_transfer=pk)
            save_qury=form_card.save(commit=False)
            save_qury.id_transfer_d=pk
            for i in qury:
                nams=i.name_send
                q=i.id_user_sender
                phs=i.phon_send
                amo=i.amount
                cou=i.courrency
                phr=i.phon_recipient
                dats=i.date_send
                namr=i.name_recipient
                rct=i.recipient_card_type
            save_qury.name_send_d=nams
            save_qury.phon_send_d=phs
            save_qury.amount_d=amo
            save_qury.courrency_d=cou
            save_qury.date_send_d=dats
            save_qury.name_recipient_d=namr
            save_qury.phon_recipient_d=phr
            save_qury.recipient_card_type_d=rct

            save_qury.id_user_sender_d=q
            save_qury.id_user_receipt_d =request.user
            save_qury.save()
            qury.delete()
            return redirect('recipient_disactivate',pk=pk)
    else:
        form_card=form_card_recipient_2()
        qury=Transfers.objects.all()
        mana=qury.filter(id_transfer=pk)
    return render(request,'my_resipientcard.html',{'form_card':form_card })

@login_required
def new_transfers(request):
    if request.method == 'POST':
        form_trans = New_Transfers(request.POST)
        
        if form_trans.is_valid():
            transfer = form_trans.save(commit=False)
            x=True
            while x :
                quryalll=Transfers.objects.all()
                rand=random.randrange(88889877878,7798989739864,5)
                if quryalll.filter(id_transfer=rand).exists():
                    continue
                else:
                    x=False

            transfer.id_transfer =rand
            transfer.id_user_sender=request.user
            
            transfer.save()
            return redirect('list')
    else:
        form_trans = New_Transfers()
    return render(request,'exam.html',{ 'form_trans':form_trans })





class Trans_disact_ListView(ListView):
    model = Transfers_dsactvita
    context_object_name = 'list_trans_disactivate'
    template_name = 'compact-table.html'
    # paginate_by = 4

