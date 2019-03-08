from django.shortcuts import render, get_object_or_404, redirect
from .forms import sellForm
from .models import sellModel


# Create your views here.

# INJECTS FORM AND SAVED MODEL OBJECTS INTO INDEX
def index(request):
    form = sellForm(request.POST or None)
    allJunk = sellModel.objects.all()
    context = {
        'form': form,
        'allJunk': allJunk,
    }

    if form.is_valid():
        form.save()

    return render(request, 'BootCRUDApp/index.html', context)

# EDITS ITEM ON A SEPARATE PAGE AND REDIRECTS TO INDEX AND SAVES OBJECT ON SUBMIT
def editItem(request, itemID):
    print('==============================================')
    item = get_object_or_404(sellModel, pk=itemID)
    print(item.id)
    form = sellForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'BootCRUDApp/index.html', {'form': form})
