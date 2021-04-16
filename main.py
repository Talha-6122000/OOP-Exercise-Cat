#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1=Cat("Kitty1",3)
cat2=Cat("Kitty2",4)
cat3=Cat("Kitty",6)


# 2 Create a function that finds the oldest cat
def Oldestcat(age1,age2,age3):
  if(age1>age2 and age1>age3):
    print(f"So cat1 is oldest of all with the age {age1}")
  elif(age2>age1 and age2>age3):
        print(f"So cat2 is oldest of all with the age {age2}")
  else:
       print(f"So cat3 is oldest of all with the age {age3}")
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
Oldestcat(cat1.age,cat2.age,cat3.age)

# There's another way to do it 
# Let's create another function
def get_oldest_cat(*args):
  return max(args)
# Now printing 
print(f"The oldest cat is {get_oldest_cat(cat1.age,cat2.age,cat3.age)} years old")