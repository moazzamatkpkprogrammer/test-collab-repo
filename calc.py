name = input("What is your name?")
print(f"Hello, {name}")
#More changes by user 1 
age = int(input("What is your age?"))
if age<18:
    print(f"{name} not allowed")
else:
    print(f"{name} allowed")