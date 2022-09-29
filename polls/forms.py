from django.forms import ModelForm,ModelChoiceField
from .models import Question,Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(ModelForm):
    question = ModelChoiceField(queryset=Question.objects)
    class Meta:
        model = Choice
        fields = ['question','choice_text']

'''class ChoiceForm(ModelForm):
    class Meta:
        model = Choice

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('user','')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['question_text']=forms.ModelChoiceField(queryset=Question.objects.filter(owner=question))'''
