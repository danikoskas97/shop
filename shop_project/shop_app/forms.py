from django import forms
from shop_app.models import Comment, Question, Response , CommentResponse


class CommentForm(forms.ModelForm):
  class Meta:
    model   = Comment
    fields  = ['username', 'text']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'comment-username',
        'placeholder': 'username',
        'required': True
      }),
      'text': forms.Textarea(attrs={
        'id': 'comment-text',
        'placeholder': 'Write a comment here...',
        'required': True
      })
    }


class QuestionForm(forms.ModelForm):
  class Meta:
    model   = Question
    fields  = ['username', 'title', 'text']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'question-username',
        'placeholder': 'username',
        'required': True
      }),
      'title': forms.TextInput(attrs={
        'id': 'question-title',
        'placeholder': 'title',
        'required': True
      }),
      'text': forms.Textarea(attrs={
        'id': 'question-text',
        'placeholder': 'Write a question here...',
        'required': True
      })
    }


class ResponseForm(forms.ModelForm):
  class Meta:
    model   = Response
    fields  = ['username', 'text']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'response-username',
        'placeholder': 'username',
        'required': True
      }),
      'text': forms.Textarea(attrs={
        'id': 'response-text',
        'placeholder': 'Write a response here...',
        'required': True
      })
    }





class CommentResponseForm(forms.ModelForm):
  class Meta:
    model   = CommentResponse
    fields  = ['username', 'text']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'response-username',
        'placeholder': 'comment response',
        'required': True
      }),
      'text': forms.Textarea(attrs={
        'id': 'response-text',
        'placeholder': 'Write a response here...',
        'required': True
      })
    }























