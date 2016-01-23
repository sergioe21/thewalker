from django.shortcuts import render
from django.http import HttpResponse

from .models import Worker
# Create your views here.


def show(request):

	return render(request,'workers/workers_list.html',{'workers':Worker.objects.all()})

def details(request,worker_id):

	data = Worker.objects.get(pk=worker_id)
	return HttpResponse(data.first_name)


#class IndexListView(ListView):

#	template_name = 'workers_list.html'
#	model = Worker

