from django import forms
from .models import Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
    
    def save(self, post=None, author=None):
        reply_detail = super(CommentForm, self).save(commit=False)
        if post:
            reply_detail.post = post
        if author:
            reply_detail.author = author
        reply_detail.save()
        return reply_detail