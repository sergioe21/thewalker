from django.shortcuts import render
from django.http import HttpResponse

from .models import Worker
# Create your views here.


def show(request):

	return render(request,'workers/index.html',{'workers':Worker.objects.all()})

def details(request,worker_id):

	data = Worker.objects.get(pk=worker_id)

	
	return render(request,'workers/base.html',{'wk':data})




#class IndexListView(ListView):

#	template_name = 'workers_list.html'
#	model = Worker

