from django import forms
from .models import Competitor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class CompetitorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompetitorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-CompetitorForm'
        self.helper.form_class = 'CompetitorForm'
        self.helper.form_method = 'post'
        self.helper.field_class = 'mb-3'
        self.helper.label_class = 'form-label'
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Competitor
        fields = [
            'name',
            'dateOfBirth',
            'bodyweight',
            'snatchFirstAttempt',
            'cnjFirstAttempt'
        ]
        labels = {
            'dateOfBirth': 'Date of Birth',
            'snatchFirstAttempt': 'Opening Snatch',
            'cnjFirstAttempt': 'Opening Clean & Jerk'
        }
    
    