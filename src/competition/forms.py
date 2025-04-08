from django import forms
from .models import Competitor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CompetitorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompetitorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-CompetitorForm'
        self.helper.form_class = 'CompetitorForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add'))

    class Meta:
        model = Competitor

        #We only need snatch and cnj first attempt to create a competitor
        fields = [
            'name',
            'date_of_birth',
            'gender',
            'bodyweight',
            'snatch_attempt_1',
            'cnj_attempt_1'
        ]

        #This just helps the user understand what information is being asked for
        labels = {
            'date_of_birth': 'Date of Birth',
            'snatch_attempt_1': 'Opening Snatch',
            'cnj_attempt_1': 'Opening Clean & Jerk'
        }
    