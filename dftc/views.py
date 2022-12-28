# dftc/views.py

from django.shortcuts import render

from .forms import StateForm

def dashboard(request):
    return render(request, "base1.html")

def display(request):
    return render(request, "stateDisplay.html")

def get_state(request):
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():

            states = []
            count = 0;

            # Open states.txt, read each state into array
            with open('states.txt', 'r') as f:
                for line in f.readlines():
                    states[count+=1]

            # Determine if user input matches an item in states arr
            for x in states:
                # if match is found, display template
                if your_state == states[x]
                    return render(request, "StateDisplay.html", {'form': form})

            return render(request, "baseErr.html")


