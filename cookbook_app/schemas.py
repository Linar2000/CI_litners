from pydantic import BaseModel


class BaseRecipe(BaseModel):
    title: str 
    count_of_view: int 
    time_cook: int 
    list_of_ingredients: str 
    description: str


class RecipeIn(BaseRecipe):
    ...


class RecipeOut(BaseRecipe):
    id: int

    class Config:
        from_attributes = True


class PrewRecipe(BaseModel):
    title: str
    count_of_view: int
    time_cook: int

    class Config:
        from_attributes = True