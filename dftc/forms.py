from django import forms


class StateForm(forms.Form):
    your_state = forms.CharField(label='Your state', max_length=30)

    states = []
    count = 0;

    with open('states.txt', 'r') as f:
        for line in f.readlines():
            states[count+=1]

    for x in states:
        if your_state == states[x]
            return true
        else
            return false

