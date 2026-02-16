import random
chicken = "Chicken"
beef = "Beef"
steak = "Steak"
pork = "Pork"
turkey = "Turkey"
lamb = "Lamb"
Meats = [chicken, beef, steak, pork, turkey, lamb]
Fillings = ["Rice", "Black beans","Pinto beans"]
Cheese = ["Cheddar", "Mozzarella", "Swiss", "Brie", "Feta", "Parmesan", "Velveeta", "Gouda"]
Sauses = ["Guac","Sour cream","Chipotle ranch","Queso","Salsa","Tomatillo salsa"]
Spices = ["Pepper", "Cumin", "Taco seasoning", "Turmeric", "Paprika", "Salt"]
Tortilla_Wrap = ["Flour tortilla", "Corn tortilla", "Chili Tortilla", "Garlic Herb Totilla", "Tomato Tortilla", "Sun-Dried Tortilla"]
Seafood_toppings = ["Shellfish", "Oyster Sauce", "Clam", "Tartar Sause"]



def meats_burr():
    print("\n Your Meat is: ",random.choice(Meats))
def fillings_burr():
    print("\n Your Filling is: ",random.choice(Fillings))
def cheeses_burr():
    print("\n Your Cheese is: ",random.choice(Cheese))
def sauses_burr():
    print("\n Your Sauce is:",random.choice(Sauses))
def spices_burr():
    print("\n Your Spice is", random.choice(Spices))
def wrap_burr():
    print("\n Your Wrap is", random.choice(Tortilla_Wrap))

meat_preference = input("Out of these options, which one do you favor over the others? \n Chicken, Beef, Steak, Pork, Turkey, Lamb, or Random. ").lower() 
if meat_preference == "chicken" :
    meat_preference = "Chicken"
if meat_preference == "beef":
    meat_preference = "Beef"
if meat_preference == "steak":
    meat_preference = "Steak"
if meat_preference == "pork" :
    meat_preference = "Pork"
if meat_preference == "turkey":
    meat_preference = "Turkey"
    meat_preference = "Lamb"
elif meat_preference == "random":
    meat_preference = random.choice(Meats)
else:
    print("Not an option")
allergies = input("Are you vegan or vegitarian? If not, put none.  ").lower()
seafood = input("Do you want Seafood options? ")
print("Burrito: ")
if allergies == "vegitarian":
    cheeses_burr()
    fillings_burr()
    sauses_burr()
    spices_burr()
    wrap_burr()
elif allergies == "vegan":
    fillings_burr()
    sauses_burr()
    spices_burr()
    wrap_burr()
else:
    print(" Your Meat is:  ", meat_preference) 
    cheeses_burr()
    fillings_burr()
    sauses_burr()
    spices_burr()
    wrap_burr()
if seafood == "yes":
    print(" Your Seafood is: ", random.choice(Seafood_toppings))
else:
    print("No Seafood choice")

def cost(a,b,c,d,e,f,g):
    if allergies == "vegan" and seafood == "yes":
        return c + d + e + f + g
    elif allergies == "vegitarian" and seafood == "yes":
            return b + c + d + e + f + g
    elif allergies == "vegan" and seafood == "no":
            return c + d + e + f
    elif allergies == "vegitarian" and seafood == "no":
            return b + c + d + e + f
    elif allergies == "none" and seafood == "yes":
         return a + b + c + d + e + f + g
    elif allergies == "none" and seafood =="no":
         return a + b + c + d + e + f
    else:
         return 0


total_cost = cost(4,3,3,2,1.5,2,4)
if total_cost == 0:
    print("Error in options")
else:
    print(f"\nTotal cost: {total_cost}")