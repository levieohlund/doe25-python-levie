#olika listor och metoder

print("=== Startar programmet ===")

#append metoden
print("\n1. APPEND metoden:")
fruits = ["apple", " banana", "grape", "pear"]
# append funktionen är till för att lägga till någon i listan 
fruits.append("orange")
print(fruits)


#clear metoden tar bort alla element i listan
print("\n2. CLEAR metoden:")
fruits = ["apple", " banana", "grape", "pear"]
fruits.clear()
print(fruits)


#copy metoden skapar en kopia av listan
print("\n3. COPY metoden:")
fruits = ["apple", " banana", "grape", "pear"]
fruits.append("orange")
x = fruits.copy()
print(x)


#sort metoden sorterar listan i bokstavsordning, la även till append för att visa att orange hamnar sist
print("\n4. SORT metoden:")
fruits = ["grape", " apple", "banana", "pear"]
fruits.sort()
fruits.append("orange")
print(fruits)


#count metoden räknar hur många gånger ett element finns i listan
print("\n5. COUNT metoden:")
fruits = ["apple", " banana", "grape", "pear"]
fruits.append("apple")  # Lägger till apple 
x = fruits.count("apple") 
print(x)