from pydantic import BaseModel, ValidationError

class Dog(BaseModel):
    name: str
    breed: str
    color: str
    age: int

def get_user_input():
    try:
        name = input("Enter the dog's name: ")
        breed = input("Enter the dog's breed: ")
        color = input("Enter the dog's color: ")
        age = int(input("Enter the dog's age: "))  # Convert the input to an integer

        # Create an instance of the Dog class with the provided input
        dog = Dog(name=name, breed=breed, color=color, age=age)
        print(dog)
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")
    except ValidationError as e:
        print("Validation error:", e)

# Run the function to get user input and create a Dog instance
get_user_input()
