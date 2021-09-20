from django.shortcuts import render

from Form.forms import PersonForm

# Create your views here.
def form_app(request):
    content = {'form' : PersonForm()}
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', content)