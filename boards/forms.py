from django import forms
from .models import Topic,Board,Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'Enter some discription '}),max_length=4000,
                            help_text= " "\
                         "Enter some text but you can't enter more than 4000 character's")

    class Meta:
        model = Topic
        fields = ['subject','message']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message',]
