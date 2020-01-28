from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
	return render(request, 'index.html')



def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user=auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Invalid credentials!')
			return redirect('/')
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
				print('user created')
				return redirect('participants:signin')
		else:
			messages.info(request, 'Sorry! The two asswords did not match!')
			return redirect('/')
		return redirect('/')
		
	else:
		return render(request, 'participants/signup.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def profile(request):
	user_id = request.user  #this object will store all the values of the user
	user = User.objects.get(pk = user_id.id)
	context = {'user':user}
	return render(request, 'participants/profile.html', context)	

def update(request):
	user_info = request.user
	user = User.objects.get(pk=user_info.id)
	context = {'user':user}
	return render(request,'participants/update.html', context)

def updatedone(request):
	user_info = request.user
	user = User.objects.get(pk=user_info.id)

	if request.method == 'POST':
		user.username = request.POST['username']
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']

		if User.objects.filter(username=user.username).exists():
			messages.info(request, 'Sorry! The username is already taken!')
			return redirect('/')
		elif User.objects.filter(email=user.email).exists():
			messages.info(request, 'Email Taken!')
			return redirect('/')
		else:
			user.save()
			messages.info(request, 'Profile updated successfully!')
			return render(request,'index.html')

	else:
		return render(request,'index.html')


		