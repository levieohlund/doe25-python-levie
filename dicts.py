#dictonaries 

int_list = [1, 5, 3,]
#           0   1  2

for elem in int_list:
    print(elem)

print(int_list[1])

print()


d = {"alice": 25, "bob": 30 }

print(d["alice"])
print(d["bob"])

print()

for key in d:
    print(key)
#varje nyckel 

print()

for val in d.values():
    print(val)
#värdena man får tilbaka

for k, val in d.items():
    print(key, val)

name = input("name to look up :")

#Appoach 1
age = d.get(name, None) #Returns None if key is missing

print(age)

#kontrollera i en if sats om ett visst nyckekvärde finns i dicts

#approach 2

if name in d:
    print(d[name])
else:
    print(f"key {name} doesn't exist in the dict.")

#Approach 3

while True:
    try:
        print(d[name])
        break
    except:
        print(f"key {name} not in dict.")
        name = input("Please enter a new, existing name: ")
