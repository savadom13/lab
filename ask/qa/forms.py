from django import forms
from .models import Question,Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField()
    question_id = forms.IntegerField(widget=forms.HiddenInput)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        #answer.question_id = self.
        answer.save()
        return answer
