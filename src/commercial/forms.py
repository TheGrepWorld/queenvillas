from django import forms

type_choices = (('booth', 'Booth'), ('showroom', 'Showroom'), ('cp', 'Commercial Plot'))
price_choice = (
    ('3000000', 'Less Than 30,00,000'), ('5000000', '30,00,000 - 50,00,000'), ('10000000', '50,00,000 - 1,00,00,000'),
    ('100000001', 'More than 1,00,00,000'))
proprty_sr = (('sell', 'SELL'), ('rent', 'RENT'))


class Filterform(forms.Form):
    type = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={"class": "custom-radio-lists", 'onchange': "location = finalurl(this.value);"}),
        choices=type_choices)
    price = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={"class": "custom-radio-lists", 'onchange': "location = finalurl1(this.value);"}), choices=price_choice)
    proprty_srt = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={"class": "custom-radio-lists", 'onchange': "location = finalurl2(this.value);"}), choices=proprty_sr)

    def clean_email(self):
        type = self.cleaned_data.get("type")
        return type
