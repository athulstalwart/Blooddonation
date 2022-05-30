from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Center


def person_create_view(request):
    form = PersonCreationForm()

    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    return render(request, 'donate.html', {'form': form},)


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'donate.html', {'form': form})


# AJAX
def load_center(request):
    district_id = request.GET.get('district_id')
    centers = Center.objects.filter(district_id=district_id).all()
    return render(request, 'center.html', {'centers': centers})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def display(request):
    return render(request,'details.html')