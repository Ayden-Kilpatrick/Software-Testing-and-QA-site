print("Enter your weight in pounds")
weight = int(input())
weight = weight * 0.45
print("Enter you height in inches")
height = float(input())
height = height * 0.025
x = weight/float(height*height)
if x < 18.5:
    print("BMI = ",x,'Under weight')
if x>=18.5 and x<25:
    print("BMI = ",x,"Normal weight")
if x >= 25 and x < 30:
   print("BMI = ",x,'Over weight')
if x >= 30:
   print("BMI = ",x,'Obese')
