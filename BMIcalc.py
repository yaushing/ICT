def calcBMI(height, weight):
    weight
    heightsqr = (height/100) ** 2
    BMI = (weight/heightsqr)
    if BMI < 18.5:
        risk = "Possible nutritional deficiency and osteoporosis."
        Cat = "Underweight"
    elif BMI <= 22.9:
        risk = "Low Risk (healthy range)"
        Cat = "Normal"
    elif BMI <= 27.4:
        risk = "Moderate risk of developing heart disease, high blood pressure, stroke, diabetes mellitus."
        Cat = "Mild to moderate overweight"
    else:
        risk = "High risk of developing heart disease, high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome."
        Cat = "Very overweight to obese"
    return risk, Cat, round(BMI, 1)

def parse_int(input):
    try:
        int(input)
        if int(input) < 100:
            return False
        return True
    except:
        return False

def parse_float(input):
    try:
        float(input)
        return True
    except:
        return False

weight = input("Weight in kg: ")
while not parse_float(weight):
    weight = input("Weight in kg: ")
weight = float(weight)
height = input("Height in cm (no decimal): ")
while not parse_int(height):
    height = input("Height in cm (no decimal): ")
height = int(height)
risk, Cat, BMI = calcBMI(height, weight)[0], calcBMI(height, weight)[1], calcBMI(height, weight)[2]
print(f"You are {Cat}. You have {risk} Your BMI is {BMI}")
    
''''
Underweight	< 18.5	Possible nutritional deficiency and osteoporosis.
Normal	18.5 – 22.9	Low risk (healthy range).
Mild to moderate overweight	23.0 – 27.4	Moderate risk of developing heart disease, high blood pressure, stroke, diabetes mellitus.
Very overweight to obese	≥ 27.5	High risk of developing heart disease, high blood pressure, stroke, diabetes mellitus. Metabolic Syndrome.
'''