from django.shortcuts import render, redirect
from shop_app.models import Product, Customer, Comment, Question, Response, CommentResponse
from shop_app.forms import CommentForm, QuestionForm, ResponseForm,CommentResponseForm
import datetime



def index(request):
  user = None
  if request.user.is_authenticated:
    user = request.user
    
  products = Product.objects.all()[:20]
  return render(request, 'index.html', context={ 'products': products, 'user': user })





def product(request, product_id):
  product = Product.objects.get(id=product_id)
  comments = Comment.objects.all().filter(product_id=product_id)
  questions = Question.objects.all().filter(product_id=product_id)

  questions_with_responses = []
  for question in questions:
    question_with_responses = {
      'question': question,
      'responses': Response.objects.all().filter(question_id=question.id)
    }

    questions_with_responses.append(question_with_responses)

  
  comments_with_commentresponses = []
  for comment in comments:
    comment_with_commentresponses = {
      'comment': comment,
      'commentresponses': CommentResponse.objects.all().filter(comment_id=comment.id)
    }

    comments_with_commentresponses.append(comment_with_commentresponses)


  return render(request, 'product.html', context={
      'product': product,
      'comments': comments_with_commentresponses,
      'questions': questions_with_responses,
    })


def customers(request):
  customers = Customer.objects.all()[:20]
  return render(request, 'customers.html', context={ 'customers': customers })


def customer(request, customer_id):
  customer = Customer.objects.get(id=customer_id)
  return render(request, 'customer.html', context={ 'customer': customer })



def comment_form(request, product_id):
  if request.method == 'POST':
    username = request.POST.get('username')
    text = request.POST.get('text')
    product = Product.objects.get(id=product_id)
    date = datetime.datetime.now()
    Comment.objects.get_or_create(username=username, text=text, date=date, product=product)

  return render(request, 'comment_form.html', context={ 'comment_form': CommentForm() })


def question_form(request, product_id):
  if request.method == 'POST':
    username = request.POST.get('username')
    text = request.POST.get('text')
    title = request.POST.get('title')
    product = Product.objects.get(id=product_id)
    Question.objects.get_or_create(username=username, text=text, title=title, product=product)
    return redirect( '/shop_app/products/{}'.format(product_id) )

  return render(request, 'question_form.html', context={ 'question_form': QuestionForm() })


def response_form(request, question_id):
  if request.method == 'POST':
    username = request.POST.get('username')
    text = request.POST.get('text')
    question = Question.objects.get(id=question_id)
    Response.objects.get_or_create(username=username, text=text, question=question)
    return redirect( '/shop_app/products/{}'.format(question.product.id) )

  return render(request, 'response_form.html', context={ 'response_form': ResponseForm() })


def commentresponse_form(request, comment_id):
  if request.method == 'POST':
    username = request.POST.get('username')
    text = request.POST.get('text')
    comment = Comment.objects.get(id=comment_id)
    CommentResponse.objects.get_or_create(username=username, text=text, comment=comment)
    return redirect( '/shop_app/products/{}'.format(comment.product.id) )

  return render(request, 'comment_response_form.html', context={ 'commentresponse_form': CommentResponseForm() })


def commentresponse_form(request, comment_id):
  if request.method == 'POST':
    username = request.POST.get('username')
    text = request.POST.get('text')
    comment = Comment.objects.get(id=comment_id)
    CommentResponse.objects.get_or_create(username=username, text=text, comment=comment)
    return redirect( '/shop_app/products/{}'.format(comment.product.id) )

  
  


















