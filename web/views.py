from django.shortcuts import render, HttpResponseRedirect
from web.forms import TicketForm
from web.models import Ticket
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method =='POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            res = Ticket.objects.create(**form.cleaned_data)
            messages.success(request, "Your data has been saved!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = TicketForm()
        
    return render(request, 'index.html', {'form': form})

def listado(request):
    tickets = Ticket.objects.all()
    return render(request, 'listado.html', {'tickets': tickets})

def setticketstate(request):
    Ticket.objects.filter(pk=request.POST.get("ticket_id")).update(ticket_state=1)
    return HttpResponseRedirect('/listado/')