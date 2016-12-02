from django import forms
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from .models import Question,Answer,User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def __init__(self, user = 'Anonimus', **kwargs):
    #     self._user = user
    #     super(AskForm, self).__init__(**kwargs)
    #
    #
    # def clean(self):
    #     if not self._user.is_active:
    #         raise forms.ValidationErroer(u"Access denied")

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        # self.cleaned_data["author"] = self._user
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField(widget=forms.HiddenInput)
    #
    # def __init__(self, *args, **kwargs):
    #     self._user = kwargs.get('user')
    #     super(AnswerForm, self).__init__(*args)

    # def clean(self):
        # pass
    #     if not self._user.is_active:
    #         raise forms.ValidationErroer(u"Access denied")

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Question number incorrect',
                                        code='validation_error')
        return question

    def save(self):
        self.cleaned_data['question'] = get_object_or_404(
            Question, pk=self.cleaned_data['question'])
        # self.cleaned_data['author'] = get_object_or_404(
        #     User, pk=self.cleaned_data['author'])

        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        #answer.question_id = self.
        # self.cleaned_data["author"] = self._user
        # answer.author_id = self._user
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