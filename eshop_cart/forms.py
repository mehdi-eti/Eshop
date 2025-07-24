from django import forms


class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1,
    )

    def clean_count(self):
        count = self.cleaned_data.get('count')
        if count <= 0:
            raise forms.ValidationError('somthing wrong')
        return count
