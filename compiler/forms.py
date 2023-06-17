from django import forms


class CppCodeForm(forms.Form):
    cppCode = forms.CharField(widget=forms.Textarea)
