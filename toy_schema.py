from pydantic import BaseModel, Field, ValidationError, root_validator
from typing import Optional

class Dimensions(BaseModel):
    length: float = Field(..., description="The length of the toy in cm")
    width: float = Field(..., description="The width of the toy in cm")
    height: float = Field(..., description="The height of the toy in cm")

    class Config:
        strict = True

class Toy(BaseModel):
    name: str = Field(..., description="The name of the toy")
    category: Optional[str] = Field(None, description="The category of the toy")
    price: float = Field(..., gt=1, lt=100, description="The price of the toy, must be between 1 and 100")
    manufacturer: Optional[str] = Field(None, description="The manufacturer of the toy")
    in_stock: bool = Field(..., description="Whether the toy is in stock")
    dimensions: Dimensions = Field(..., description="The dimensions of the toy")

    @root_validator
    def check_dimensions(cls, values):
        dimensions = values.get('dimensions')
        if dimensions:
            if not (dimensions.length < 10 and dimensions.width < 50 and dimensions.height < 100):
                raise ValueError("Dimensions must be: length < 10, width < 50, height < 100")
        return values

    class Config:
        strict = True

# Example usage with strict mode
try:
    toy_example = Toy.model_validate({
        'name': 'Toy Car',
        'category': 'Vehicles',
        'price': 19.99,
        'manufacturer': 'ToyMaker Inc.',
        'in_stock': True,
        'dimensions': {
            'length': 9.5,
            'width': 49.5,
            'height': 99.0
        }
    }, strict=True)
    print(toy_example)
except ValidationError as exc:
    print(exc)
