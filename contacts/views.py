from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if already made
        if request.user.is_authenticated:
            user_id = request.user.id
            contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if contacted:
                messages.error(request, 'already made')
                return redirect('/listings/'+listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        # # send mail
        # send_mail(
        #     'Property Listing inquiry',
        #     'There has been an inquiry for ' + listing +
        #     '. Sign into admin panel for more info',
        #     'coolansh.911@gmail.com',
        #     [realtor_email, 'coolansh.911@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Request submit, realtor contact you soon')

        return redirect('/listings/'+listing_id)
