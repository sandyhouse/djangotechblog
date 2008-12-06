from django import forms


class CommentForm(forms.Form):

    name = forms.CharField(label="Name (required)", required=True)
    email = forms.EmailField(label="Email (required)", required=False)
    url = forms.CharField(label="Website", required=False)
    content = forms.CharField(label="Comment", widget=forms.Textarea(), required=True)


    content_type = forms.CharField(widget=forms.HiddenInput(), required=True)
    object_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)