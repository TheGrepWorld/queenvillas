from django import forms

bhk_choices = (('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
price_choice = (('3000000','Less Than 30,00,000'),('5000000','30,00,000 - 50,00,000'),('10000000','50,00,000 - 1,00,00,000'),('100000001','More than 1,00,00,000'))

class Filterform(forms.Form):
    bhks = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class":"custom-radio-lists", 'onchange' : "location = finalurl(this.value);"}), choices=bhk_choices)
    price = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class":"custom-radio-lists", 'onchange' : "location = finalurl1(this.value);"}), choices=price_choice)

    def clean_email(self):
        bhks = self.cleaned_data.get("bhks")
        return bhks
