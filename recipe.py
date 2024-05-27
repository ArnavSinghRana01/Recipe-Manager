import json
import os

RECIPE_FILE = "recipes.json"

def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as f:
        json.dump(recipes, f, indent=4)

def add_recipe():
    title = input("Enter recipe title: ")
    ingredients = input("Enter ingredients (comma separated): ")
    instructions = input("Enter instructions: ")

    recipe = {
        'title': title,
        'ingredients': [ingredient.strip() for ingredient in ingredients.split(',')],
        'instructions': instructions.strip(),
    }

    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")

def update_recipe():
    title = input("Enter the title of the recipe to update: ")
    recipes = load_recipes()
    
    for recipe in recipes:
        if recipe['title'].lower() == title.lower():
            print(f"Current ingredients: {', '.join(recipe['ingredients'])}")
            new_ingredients = input("Enter new ingredients (comma separated): ")
            new_instructions = input("Enter new instructions: ")

            recipe['ingredients'] = [ingredient.strip() for ingredient in new_ingredients.split(',')]
            recipe['instructions'] = new_instructions.strip()

            save_recipes(recipes)
            print("Recipe updated successfully!")
            return
    
    print("Recipe not found!")

def delete_recipe():
    title = input("Enter the title of the recipe to delete: ")
    recipes = load_recipes()
    new_recipes = [recipe for recipe in recipes if recipe['title'].lower() != title.lower()]
    
    if len(new_recipes) < len(recipes):
        save_recipes(new_recipes)
        print("Recipe deleted successfully!")
    else:
        print("Recipe not found!")

def view_recipes():
    recipes = load_recipes()
    
    if not recipes:
        print("No recipes found!")
        return
    
    for recipe in recipes:
        print(f"Title: {recipe['title']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")
        print("-" * 20)

def main():
    while True:
        print("\nRecipe Book Manager")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. View Recipes")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_recipe()
        elif choice == "2":
            update_recipe()
        elif choice == "3":
            delete_recipe()
        elif choice == "4":
            view_recipes()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
