from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm


def home(request):
  chais = ChaiVarity.objects.all()
  return render(request, 'chai/chai.html', {'chais':chais})

def details(request, chai_id):
  chai = get_object_or_404(ChaiVarity, pk=chai_id)
  return render(request, 'chai/detail.html', {'chai':chai})

def chai_store(request):
  
  store = None
  if request.method == 'POST':
    form = ChaiVarityForm(request.POST)
    if form.is_valid():
      chai_varity = form.cleaned_data['chai_varity']
      store = Store.objects.filter(chai_varieties = chai_varity)
  else:
    form = ChaiVarityForm()
    
  return render(request, 'chai/chai_stores.html', {'store':store, 'form':form})