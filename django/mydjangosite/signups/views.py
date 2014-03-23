from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.core.urlresolvers import reverse
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "感谢您的加入！")
        return redirect(reverse('signups:thank-you'))

    return render_to_response('signups/signup.html',
                              locals(),
                              context_instance=RequestContext(request))
    #return render(request, 'signups/signup.html')


def thank_you(request):
    return render(request, 'signups/thankyou.html')

def about_us(request):
    return render(request, 'signups/aboutus.html')