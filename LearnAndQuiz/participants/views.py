from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import participants_update_form, profile_update_form
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'index.html')



def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user=auth.authenticate(username=username, password=password)
		# if the user already has account
		if user is not None: 
			auth.login(request, user)
			return redirect('/') #redirects to the homepage/index page	
		else:
			messages.info(request, 'Invalid credentials!')
			return redirect('participants:signin')
	else:
		return render(request, 'participants/signin.html')


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Sorry! The username is already taken!')
				return redirect('/')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Sorry! The email is already in use!')
				return redirect('/')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				messages.success(request, "Account created for " + username + "." + " Please Login to continue.")
				return redirect('participants:signin')
		else:
			messages.info(request, 'Sorry! The two passwords did not match!')
			return redirect('/')
		return redirect('/')
		
	else:
		return render(request, 'participants/signup.html')

def logout(request):
	auth.logout(request)
	return redirect('/')


@login_required(login_url="/signin/")
def profile(request):
	if request.method == 'POST':
		participants_form = participants_update_form(request.POST, instance=request.user) #gets username & email form participants_update_form and stores in declared var
		profile_form = profile_update_form(request.POST, request.FILES, instance=request.user.profile) #gets image from profile_update_form

		user= request.POST['username']

		if participants_form.is_valid and profile_form.is_valid(): #checks form validity
			if User.objects.filter(username=user).exists(): #cecks if username already exists
				if request.user.username== user : #if the username is same as before, save it. Helps in updating single field
					participants_form.save()
					profile_form.save()
					messages.info(request, 'Your account has been updated!')
					return redirect('participants:profile')
				else:	
					messages.info(request, 'Sorry! The username is already taken!')
					return redirect('participants:profile')

			else:	
				participants_form.save()
				profile_form.save()
				messages.info(request, 'Your account has been updated!')
				return redirect('participants:profile')
	else:
		participants_form = participants_update_form(instance=request.user) #shows user info in input field like placeholder
		profile_form = profile_update_form()
	context={
		'participants_form': participants_form,
		'profile_form': profile_form
	}
	return render(request, 'participants/profile.html', context)	



		