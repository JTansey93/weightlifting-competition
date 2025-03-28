M_WEIGHT_CLASSES = [55, 61, 67, 73, 81, 89, 96, 102]
F_WEIGHT_CLASSES = [48, 53, 58, 63, 69, 77, 86]

class Competitor():

    def __init__(self, name, gender, dob, bodyweight):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.bodyweight = bodyweight
        self.snatch_attempts = [[0, False], [0, False], [0, False]]
        self.cnj_attempts = [[0, False], [0, False], [0, False]]

        if self.gender == "M":
            for i in range(M_WEIGHT_CLASSES):
                if self.bodyweight >= M_WEIGHT_CLASSES[i]:
                    self.weight_class = str(M_WEIGHT_CLASSES[i]) + "kg"
            self.weight_class =  "+102kg"

        if self.gender == "F":
            for i in range(F_WEIGHT_CLASSES):
                if self.bodyweight >= F_WEIGHT_CLASSES[i]:
                    self.weight_class = str(F_WEIGHT_CLASSES[i]) + "kg"
            self.weight_class =  "+86kg"

    def snatch(self, attempt_no, weight, make):
        self.snatch_attempts[attempt_no] = [weight, make]

    def cnj(self, attempt_no, weight, make):
        self.cnj_attempts[attempt_no] = [weight, make]
            
    def sinclair(self):
        pass