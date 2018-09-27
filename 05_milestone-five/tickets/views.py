from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from .forms import TicketForm
from .models import Ticket, Comment

# Create your views here.

def return_tickets(request):
    """
    Return the tickets.html template, displays current tickets and a form to allow new tickets to be created
    """
    
    # All created tickets 
    tickets = Ticket.objects.all()
    comments = Comment.objects.all()
    
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect(reverse('return_tickets'))
    
    else:
        ticket_form = TicketForm()
    
    return render(request, "tickets.html", { "form": ticket_form , "tickets": tickets , "comments": comments } )
    
    
def add_comment(request, id):
    """
    Add a comment posted in tickets.html to the associated ticket using its id
    """
    current_ticket = Ticket.objects.get(pk = id)
    
    if request.method == "POST":
        # Create new Comment instance using the POST request and storing value in the current_ticket variable
        comment = Comment.objects.create(comment = request.POST['comment'], ticket = current_ticket)
        
    return redirect(reverse('return_tickets') )