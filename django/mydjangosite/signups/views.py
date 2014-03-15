from django.shortcuts import render, render_to_response, RequestContext
from .forms import SignUpForm


# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response('signups/signup.html',
                              locals(),
                              context_instance=RequestContext(request))
    #return render(request, 'signups/signup.html')