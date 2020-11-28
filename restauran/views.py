from django.shortcuts import render
from .models import MostRecent,Feedback
def home_page(request):
    items = MostRecent.objects.all()
    feedback = Feedback.objects.all()
    context = {
        'items':items,
        'feedback':feedback
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def order(request,item_id):
    mstOrder = MostRecent.objects.get(id=item_id)
    context = {
        'mstOrder':mstOrder
    }
    return render(request,'order.html',context)
