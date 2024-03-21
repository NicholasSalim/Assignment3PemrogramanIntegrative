class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

weight = float(input("Masukkan berat Anda (kg): "))
height = float(input("Masukkan tinggi Anda (meter): "))


person = BMI(weight, height)

bmi = person.BMI_Value()

print("BMI Anda:", bmi)
