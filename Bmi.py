name1 = "kk"
height_m1 = 5
weight_kg1 = 50

name2 = "kk's sister"
height_m2 = 2.1
weight_kg2 = 55

name3 = "kk's brother"
height_m3 = 3.1
weight_kg3 = 45

def bmi_calculator(name, height_m,weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight "
    else:
        return name + " is overweight "

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)



    
    



    


