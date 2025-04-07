from sqlalchemy import Column, Integer, String
from database import Base

class RecipeModel(Base):
    __tablename__ = 'Recipe'

    id = Column(Integer, primary_key=True)

    title = Column(String(100), nullable=False)
    count_of_view = Column(Integer, default=0, nullable=False)
    time_cook = Column(Integer, default=0, nullable=False)
    list_of_ingredients = Column(String, nullable=False)
    description = Column(String, nullable=False)
