from django import forms


class TextForm(forms.Form):
    CHOICES = [('qr_code', 'Qr Code'),
               ('Code128', 'Barcode Code128'),
               ('Gs1_128', 'Barcode Gs1_128'),
               ('CODABAR', 'Barcode CODABAR')]

    barcode_type_selection = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.Select(attrs={'id': 'qr_type_input_id','class': 'barcode_type_css'}))