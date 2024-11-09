from typing import List

class Entity:
    pass

class Food:

    def __init__(self, amount_per_instance: float):
        #self.amount_per_instance = amount_per_instance
        self.amount_left = amount_per_instance
        self.visible = True if self.amount_left > 0 else False  

    
class Scene:
    """A scene in which a simulation is to be run"""

    def __init__(self, food_count, entities: List[Entity]):
        self.food_count = food_count
        self.entities = len(entities)
        self.entity_per_food = 2
        self.food = None

    def eat_food(self, food: Food, amount: float):
        food.amount_left -= amount        

    def spawn_food(self):
        """Spawn food in the scene based on the food count"""
        self.food = [Food(i) for i in range(self.food_count)]

