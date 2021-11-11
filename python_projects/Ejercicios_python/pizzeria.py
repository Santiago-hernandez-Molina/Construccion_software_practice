""" Pizza  Bella Napoli """
print("----------Pizza Bella Napoli-------------\n")

vegetarian: bool
ingredients = ['mozzarella', 'tomate']
vegetarian_ingredients = ['Pimiento', 'tofu']
no_vegetarian_ingredients = ['Peperoni', 'Jamón', 'Salmón']

if input(" Ingrese el tipo de pizza (Vegetariana, no vegetariana): ").lower() == 'vegetariana':
    ingredients.append(input(f" \nElija un ingrediente de la pizza vegetariana:\n  {vegetarian_ingredients}\n"))
    vegetarian = True
else:
    ingredients.append(input(f" \nElija un ingrediente de la pizza no vegetariana:\n  {no_vegetarian_ingredients}\n"))
    vegetarian = False

print(f"\nLa pizza elegida es {'vegetariana' if vegetarian else 'no vegetariana'} y sus ingredientes son:"
      f"\n{ingredients}")