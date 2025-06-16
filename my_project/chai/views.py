from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity


def home(request):
  chais = ChaiVarity.objects.all()
  return render(request, 'chai/chai.html', {'chais':chais})

def details(request, chai_id):
  chai = get_object_or_404(ChaiVarity, pk=chai_id)
  return render(request, 'chai/detail.html', {'chai':chai})