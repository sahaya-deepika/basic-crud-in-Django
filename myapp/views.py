from django.shortcuts import render, redirect
from .forms import PatientForm

def enter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = PatientForm()
    return render(request, 'myapp/patient_form.html', {'form': form})

def thank_you(request):
    return render(request, 'myapp/thank_you.html')

