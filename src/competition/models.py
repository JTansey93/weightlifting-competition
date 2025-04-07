from django.db import models
import math

# Create your models here.

class Competitor(models.Model):
    name = models.CharField(max_length=32)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    bodyweight = models.DecimalField(max_digits=5, decimal_places=2)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    snatch_attempt_1 = models.IntegerField()
    snatch_attempt_1_make = models.BooleanField(null=True, blank=True)
    snatch_attempt_2 = models.IntegerField(null=True, blank=True)
    snatch_attempt_2_make = models.BooleanField(null=True, blank=True)
    snatch_attempt_3 = models.IntegerField(null=True, blank=True)
    snatch_attempt_3_make = models.BooleanField(null=True, blank=True)

    cnj_attempt_1 = models.IntegerField()
    cnj_attempt_1_make = models.BooleanField(null=True, blank=True)
    cnj_attempt_2 = models.IntegerField(null=True, blank=True)
    cnj_attempt_2_make = models.BooleanField(null=True, blank=True)
    cnj_attempt_3 = models.IntegerField(null=True, blank=True)
    cnj_attempt_3_make = models.BooleanField(null=True, blank=True)

    @property
    def weight_class(self):
        M_WEIGHT_CLASSES = [55, 61, 67, 73, 81, 89, 96, 102]
        F_WEIGHT_CLASSES = [48, 53, 58, 63, 69, 77, 86]
        if self.gender == "M":
            for i in range(len(M_WEIGHT_CLASSES)):
                if self.bodyweight >= M_WEIGHT_CLASSES[i]:
                    return str(M_WEIGHT_CLASSES[i]) + "kg"
            return "+102kg"

        if self.gender == "F":
            for i in range(len(F_WEIGHT_CLASSES)):
                if self.bodyweight >= F_WEIGHT_CLASSES[i]:
                    return str(F_WEIGHT_CLASSES[i]) + "kg"
            return "+86kg"

    @property
    def total(self):
        if self.snatch_attempt_1_make == True:
            best_snatch =  self.snatch_attempt_1
        elif self.snatch_attempt_2_make == True:
            best_snatch = self.snatch_attempt_2
        elif self.snatch_attempt_3_make == True:
            best_snatch = self.snatch_attempt_3_make
        else:
            return None
        
        if self.cnj_attempt_1_make == True:
            best_cnj =  self.cnj_attempt_1
        elif self.cnj_attempt_2_make == True:
            best_cnj = self.cnj_attempt_2
        elif self.cnj_attempt_3_make == True:
            best_cnj = self.cnj_attempt_3_make
        else:
            return None
        
        return best_snatch + best_cnj
        
    @property
    def sinclair(self):
        if self.total == None:
            return None
        elif self.gender == 'M':
            return round(self.total * (10.0**(0.722762521*(math.log10(float(self.bodyweight)/193.609))**2.0)), 2)
        elif self.gender == 'F':
            return round(self.total * (10.0**(0.787004341*(math.log10(float(self.bodyweight)/153.757))**2.0)), 2)
        else:
            return None