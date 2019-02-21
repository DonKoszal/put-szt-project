from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb','publish']

class AddComment(forms.ModelForm):
    def __init__( self, *args, **kwargs ):
        super(AddComment, self).__init__( *args, **kwargs )
        self.fields['body'].label = ''

    class Meta:
        model = models.Comment
        fields = ['body']