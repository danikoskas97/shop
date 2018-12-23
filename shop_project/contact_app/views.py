from django.shortcuts import render, redirect
from contact_app.forms import ContactForm
from contact_app.models import Contact


def contact(request):
  if request.method == 'POST':
    subject = request.POST.get('subject')
    email = request.POST.get('email')
    text = request.POST.get('text')
    Contact.objects.get_or_create(subject=subject, email=email, text=text)
    return redirect('success/')

  return render(request, 'contact.html', context={ 'contact_form': ContactForm() })


def success(request):
  return render(request, 'success.html')