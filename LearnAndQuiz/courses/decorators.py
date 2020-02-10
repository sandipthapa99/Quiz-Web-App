from django.shortcuts import redirect
from django.contrib import messages



def admin_only(func):
	def func(request, *args, **kwargs):
		group = None 
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name #[0] is the index of the group in model

		if group == "admin":
			return func(request, *args, **kwargs)

		else:
			messages.info(request, 'You do not have permission to perform this task!')
			return redirect('courses:courses')
	return func