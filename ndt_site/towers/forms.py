from django import forms



class SearchForm(forms.Form):

    tower_id = forms.CharField(label='', max_length=20)
        
        