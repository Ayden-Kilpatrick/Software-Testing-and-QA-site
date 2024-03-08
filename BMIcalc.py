print("Enter your hieght in inches")
weight = int(input())
print("Enter you wieght in pounds")
height = float(input())
x = weight/float(height*height)
if x < 18.5:
    print("BMI = ",x,'Under weight')
if x>=18.5 and x<25:
    print("BMI = ",x,"Normal weight")
if x >= 25 and x < 30:
   print("BMI = ",x,'Over weight')
if x >= 30:
   print("BMI = ",x,'Obese')
