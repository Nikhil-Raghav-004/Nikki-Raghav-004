# BMI Calculater
height=float(input("Enter your height in cms"))
weight=float(input("Enter your Weight in Kg"))

height=height/100
Ans = height*height
BMI= weight/Ans


if BMI>0 and BMI<16:
    print("You are SO UNDERWEIGHT, Eat More")
elif BMI>16 and BMI<24:
    print("You Are Fit, Great Job! ")
elif BMI>24 and BMI<30:
    print("Little overweight, Some days of working out and ur good to go!")
elif BMI>30 and BMI<35:
    print("Obese!")
else:
    print("Morbid Obese, Very High Risk of Death, Please Fix Yourself!")