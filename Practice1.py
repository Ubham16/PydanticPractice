from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    breed: str
    color: str
    age: int

# Example usage:
dog = Dog(name="Buddy", breed="Golden Retriever", color="Golden", age=5)
print(dog)
