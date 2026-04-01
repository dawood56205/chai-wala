from django.shortcuts import render
from .models import CHAIVARIETY, stores
from django.shortcuts import get_object_or_404
from .froms import chaivarietyform

# Create your views here.
def all_chai(request) :
  chais = CHAIVARIETY.objects.all()
  return render(request, 'chai/index.html', {'chais': chais})

def chai_detail(request, chai_id):
  Stores = get_object_or_404(stores, pk=chai_id)
  chai = get_object_or_404(CHAIVARIETY, pk=chai_id)
  return render(request, 'chai/chai_detail.html', {'chai': chai, 'Stores': Stores})

def chai_store(request):
  chai = CHAIVARIETY.objects.all()
  Stores = None
  if request.method == 'POST':
    forms = chaivarietyform(request.POST)
    if forms.is_valid():
      chai_variety = forms.cleaned_data['chai_variety']
      Stores = stores.objects.filter(chai_varieties = chai_variety)
  else:
    forms = chaivarietyform()

  return render(request, 'chai/chai_store.html', {'Stores' : Stores, 'forms': forms, 'chai':chai})

def contact_us(request):
  return render(request, 'chai/contact_us.html')
# def order_chai(request) :
#   return render(request, 'chai/indexorder.html')

# def lattechoices(request) :
#   return render(request, 'chai/indexchoice.html')