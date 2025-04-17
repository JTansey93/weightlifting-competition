from django import forms
from .models import Competitor

class CompetitorForm(forms.ModelForm):

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
    