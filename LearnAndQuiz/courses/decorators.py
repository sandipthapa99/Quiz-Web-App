from django.shortcuts import redirect
from django.contrib import messages



def admin_only(func):
	def inner_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == "admin":
			return func(request, *args, **kwargs)

		else:
			messages.info(request, 'You do not have permission to perform this task!')
			return redirect('/')
	return inner_func