from django.shortcuts import render
from details.models import Detail
from django.shortcuts import HttpResponseRedirect
from details.forms import DetailsForm



# Create your views here.
def index(request):

	foo = DetailsForm(request.POST or None)

	if foo.is_valid():
		foo.save(commit=True)
		foo = DetailsForm()
	else:
		foo = DetailsForm()
	
	
	context_dict = {"modelform" : foo}
	return render(request,"index.html",context_dict)

def user(request):

	return render(request,"inp.html",{"name_list": Detail.objects.all()})


