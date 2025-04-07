from fastapi import FastAPI
from sqlalchemy.future import select

from typing import List

import models
import schemas
from database import engine, session

app = FastAPI()

@app.on_event('startup')
async def shutdown():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.on_event('shutdown')
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipe/', response_model=schemas.RecipeOut)
async def create_recipe(recipe: schemas.RecipeIn) -> models.RecipeModel:
    """
    post-endpoint for recipe objects create
    :param recipe: json
    """
    new_recipe = models.RecipeModel(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe

@app.get('/recipe/', response_model=List[schemas.PrewRecipe])
async def get_all_recipe() -> List[models.RecipeModel]:
    """
    get-endpoint for get all recipes objects
    :return: list of objects
    """
    res = await session.execute(select(models.RecipeModel).order_by(models.RecipeModel.count_of_view.desc()))
    return res.scalars().all()

@app.get('/recipe/{idx}/', response_model=List[schemas.RecipeOut])
async def get_recipe_by_id(idx: int) -> List[models.RecipeModel]:
    """
    get-endpoint for get recipe objects by id
    :param idx: int
    :return: json
    """
    res = await session.execute(select(models.RecipeModel).where(models.RecipeModel.id == idx))
    recipe = res.scalars().all()
    print(recipe[0])
    recipe[0].count_of_view += 1
    await session.commit()
    return recipe