from django.db import models

# Create your models here.
class food(models.Model):
    Food_code = models.IntegerField()
    Main_food_description = models.TextField()
    WWEIA_Category_description = models.TextField()
    Energy = models.FloatField()
    Protein = models.FloatField()
    Carbohydrate = models.FloatField()
    Sugar = models.FloatField()
    Fiber = models.FloatField()
    Alcohol = models.FloatField()
    Vitamin_C = models.FloatField()
    Vitamin_A = models.FloatField()
    Vitamin_B12 = models.FloatField()
    Vitamin_D = models.FloatField()
    Calcium = models.FloatField()
    Phosphorus = models.FloatField()
    Magnesium = models.FloatField()
    Iron = models.FloatField()
    Zinc = models.FloatField()
    Selenium = models.FloatField()
    Potassium = models.FloatField()
    Sodium = models.FloatField()
    Copper = models.FloatField()
    Theobromine = models.FloatField()
    Caffeine = models.FloatField()
    Portion_description = models.TextField()
    Portion_weight = models.FloatField()
    
    def __str__(self):
        return self.Main_food_description