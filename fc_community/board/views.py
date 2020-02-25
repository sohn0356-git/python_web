from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
    
    boards = Board.objects.all().order_by('-id')
    
    return render(request,'board_list.html', {'boards':boards})