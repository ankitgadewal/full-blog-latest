from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Premium
from django.views.decorators.csrf import csrf_exempt
from users.paytm import Checksum
import random

MERCHANT_KEY = 'your merchant key'
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account is created for {username}! you can now login ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been Updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/profile.html', {'u_form':u_form, 'p_form':p_form})

@login_required
def premium_info(request):
    return render(request, 'user/premium_info.html')

order_id = random.randint(100000,10000000)

@login_required
def premium(request):
    print(request.user)
    # return render(request, 'user/premium.html')
    params_dict = {
            'MID':'wgyjVw30068262008394',
            'ORDER_ID':str(order_id),
            'TXN_AMOUNT':'930',
            'CUST_ID':request.user.email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/premium/handle_request/',
        }
    params_dict['CHECKSUMHASH'] = Checksum.generate_checksum(params_dict, MERCHANT_KEY)
    return render(request, 'user/premium.html', {'params_dict':params_dict})



@csrf_exempt
def handle_request(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print(response_dict['ORDERID'])
            print(response_dict['TXNAMOUNT'])
            print(response_dict['RESPMSG'])
            print(response_dict['MID'])
            print(response_dict['TXNID'])
            print(response_dict['BANKTXNID'])
            print(response_dict['TXNDATE'])
            print(response_dict['BANKNAME'])
            print(response_dict['PAYMENTMODE'])
            print(response_dict['STATUS'])
            print(response_dict['GATEWAYNAME'])
            print(request.user)
            

            # newpremium = Premium(order_id=order_id, charge=int(charge))
            # newpremium.save()
        else:
            print('order was not successful because of '+ response_dict['RESPMSG'])
    return render(request, 'user/paymentstatus.html', {'response': response_dict})