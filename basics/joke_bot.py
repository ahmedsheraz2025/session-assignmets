
JOKE = """Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia
returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"""

SORRY = "Sorry I only tell jokes"


user_input: str = input("Enter what you want ")

if "joke" in user_input.lower():
    print(JOKE)
    
else:
    print(SORRY)