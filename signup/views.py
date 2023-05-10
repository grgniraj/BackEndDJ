import random
from .forms import ProductForm
from login.serializers import UserSerializer
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from inventory.models import Product
from inventory.models import Admin

# Create your views here.
# def signaction(request):
#     if request.method == "POST":
#         password = request.POST['password']
#         try:
#             validate_password(password)
#         except ValidationError as e:
#             # The password entered by the user is invalid
#             # Handle the error here
#             error_message = "Invalid password. Your password must contain at least 8 characters and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
#             context = {'error_message': error_message}
#             return render(request, 'signup_page.html', context)
#         else:
#             context = {}
#             # The password entered by the user is valid
#             # Process the data here
#             # Get the form data from the request
#             full_name = request.POST['fullname']
#             email = request.POST['email']

#             cpassword = request.POST['cpassword']
#             if cpassword.__eq__(password):
#                 # Create a new ImsAdmin instance with the form data
#                 hashed_password = make_password(password)
#                 admin = User(username=full_name, email=email,
#                               password=hashed_password, is_staff=True)

#             # Save the new instance to the database
#                 status = admin.save()
#                 return render(request, 'userinfo.html', context)
#             else:
#                 error_message = "Password Mismatch!!"
#                 context = {'error_message': error_message}
#                 return render(request, 'signup_page.html', context)
#     else:
#         context = {}
#         return render(request, 'signup_page.html', context)


def signaction(request):
    if request.method == "POST":
        password = request.POST['password']
        try:
            validate_password(password)
        except ValidationError as e:
            error_message = "Invalid password. Your password must contain at least 8 characters and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
            context = {'error_message': error_message}
            return render(request, 'signup_page.html', context)
        else:
            full_name = request.POST['fullname']
            email = request.POST['email']
            cpassword = request.POST['cpassword']
            if cpassword == password:
                request.session['full_name'] = full_name
                request.session['email'] = email
                request.session['password'] = password
                return redirect('userinfo')
            else:
                error_message = "Password Mismatch!!"
                context = {'error_message': error_message}
                return render(request, 'signup_page.html', context)
    else:
        context = {}
        return render(request, 'signup_page.html', context)


def useraction(request):
    print("one")
    if request.method == "POST":
        print("two")
        full_name = request.session.get('full_name')
        email = request.session.get('email')
        password = request.session.get('password')
        date_of_birth = request.POST['date_of_birth']
        contact_number = request.POST['contact_number']
        address = request.POST['address']
        sex = request.POST['sex']
        print(full_name, email, password, date_of_birth,
              contact_number, address, sex)
        hashed_password = make_password(password)
        admin = Admin(name=full_name, email=email, password=hashed_password,
                      date_of_birth=date_of_birth, contact_number=contact_number, address=address, sex=sex)
        admin.save()

        return redirect('login')
    else:
        print("three")
        context = {}
        return render(request, 'userinfo.html', context)


def homeaction(request):
    return render(request, 'Home.html')


def aboutaction(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contactus.html')


def order(request):
    return render(request, 'orderprocessing.html')


@login_required
def dashboardaction(request):
    return render(request, 'Dash.html')

# @login_required
# def inventorytrackaction(request):
#     return render(request, 'inventory_track.html')


@login_required
def changeaction(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Updating the session after a password change, logging out all other sessions
            # for security reasons, since the old password is no longer valid.
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# for sending otp


@login_required
def forgetaction(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Generate a random 6-digit OTP
            otp = str(random.randint(100000, 999999))
            # Compose the email message
            subject = 'Your OTP for password reset'
            message = f'Your OTP is {otp}.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            # Send the email using Gmail
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=True)
            # Store the OTP in the session for later verification
            request.session['otp'] = otp
            # Render the verification page
            return render(request, 'verifyotp.html')
        else:
            error_message = 'Please enter a valid email address.'
            return render(request, 'forgotpass.html', {'error_message': error_message})
    else:
        return render(request, 'forgotpass.html')


@login_required
def UploadPictureAction(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            # Replace 'profile' with the URL name of your profile page
            return redirect('profile.html')
    else:
        serializer = UserSerializer(instance=request.user)
    return render(request, 'profile.html', {'serializer': serializer})


def inventorytrackaction(request):
    if request.method == 'POST':
        name = request.POST['productname']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        location = request.POST['location']
        reorderpoint = request.POST['reorderpoint']
        brand = request.POST['brandname']
        expdate = request.POST['expirationdate']

        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            location=location,
            reorderpoint=reorderpoint,
            brand=brand,
            expirationdate=expdate
        )
        product.save()
        # Redirect to the inventory track page after saving the product
        return redirect('inventorytrack')

    return render(request, 'inventory_track.html')


def add_item(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item added successfully!')
            return redirect('inventorytrack')
    else:
        form = ProductForm()
    return render(request, 'inventory_track.html', {'form': form})
