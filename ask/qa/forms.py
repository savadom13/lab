from django import forms
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from .models import Question,Answer,User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        if self._user:
            question.author = self._user
        else:
            question.author = get_object_or_404(User, pk=1)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Question number incorrect',
                                        code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        if self._user:
            answer.author = self._user
        else:
            answer.author = get_object_or_404(User, pk=1)
        answer.save()
        return answer

class SignupForm(ModelForm):
    class Meta:
        model = User
        exclude = ['is_active', 'is_staff']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }