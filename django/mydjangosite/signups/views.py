from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.core.urlresolvers import reverse
from .forms import SignUpForm


# Create your views here.
def home(request):

    return render_to_response('signups/signup.html',
                              locals(),
                              context_instance=RequestContext(request))
    #return render(request, 'signups/signup.html')


def thank_you(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        subject = '欢迎您的加入！'
        message = '感谢您的注册，我们随时欢迎您的下次光临！'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [save_it.email, from_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        messages.success(request, "感谢您的加入！")
        return redirect(reverse('signups:thank-you'))
    return render(request, 'signups/thankyou.html', locals())


def about_us(request):
    return render(request, 'signups/aboutus.html')