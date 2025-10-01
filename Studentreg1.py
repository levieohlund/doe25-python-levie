name = input("Whats your name?")   
age = int(input("whats your age?"))

if age  >= 18:
    print(f"{name}"" You are a adult")
else:
    print(f"{name}"" You are a minor")    

for i in range(5):
    print("Hello " + name + " you are " + str(age) + " years old")
