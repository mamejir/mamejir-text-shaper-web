from django import forms

class TextShapeForm(forms.Form):
    val1 = forms.CharField(label="ここに文章を貼り付け", widget=forms.Textarea())
