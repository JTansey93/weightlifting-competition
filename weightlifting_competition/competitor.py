import math

M_WEIGHT_CLASSES = [55, 61, 67, 73, 81, 89, 96, 102]
F_WEIGHT_CLASSES = [48, 53, 58, 63, 69, 77, 86]

class Competitor():

    def __init__(self, name, gender, dob, bodyweight, first_snatch, first_cnj):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.bodyweight = bodyweight
        self.next_snatch = first_snatch
        self.next_cnj = first_cnj
        self.snatch_attempts = [[0, False], [0, False], [0, False]]
        self.cnj_attempts = [[0, False], [0, False], [0, False]]
        self.best_snatch = 0
        self.best_cnj = 0

        if self.gender == "M":
            for i in range(len(M_WEIGHT_CLASSES)):
                if self.bodyweight >= M_WEIGHT_CLASSES[i]:
                    self.weight_class = str(M_WEIGHT_CLASSES[i]) + "kg"
            self.weight_class =  "+102kg"

        if self.gender == "F":
            for i in range(len(F_WEIGHT_CLASSES)):
                if self.bodyweight >= F_WEIGHT_CLASSES[i]:
                    self.weight_class = str(F_WEIGHT_CLASSES[i]) + "kg"
            self.weight_class =  "+86kg"

    def snatch(self, attempt_no, weight, make):
        self.snatch_attempts[attempt_no] = [weight, make]
        if make:
            self.best_snatch = weight
            if attempt_no < 3:
                self.next_snatch = weight + 1

    def cnj(self, attempt_no, weight, make):
        self.cnj_attempts[attempt_no] = [weight, make]
        if make:
            self.best_cnj = weight
            if attempt_no < 3:
                self.next_snatch = weight + 1

    def get_total(self):
        return self.best_snatch + self.best_cnj
            
    def sinclair(self):
        if self.get_total() == 0:
            return None
        elif self.gender == "M":
            return round(self.get_total() * (10.0**(0.722762521*(math.log10(self.bodyweight/193.609))**2.0)), 2)
        elif self.gender == "F":
            return round(self.get_total() * (10.0**(0.787004341*(math.log10(self.bodyweight/153.757))**2.0)), 2)
        else:
            return None