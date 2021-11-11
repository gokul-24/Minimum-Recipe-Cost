from django.db import models

# ASSUMING THAT ALL THE STORE HAVE ALL THE INGREDIENTS WITH DIFFERENT MRP 
# AND THAT THE DISCOUNT CALCUATED IS IN RUPEES AND NOT IN PERCENT

class Stores(models.Model):
    name=models.CharField(max_length=50)

    flour=models.IntegerField()                     # initial amount
    discount_flour=models.IntegerField()            # discount avaiable  
    after_discount_flour=models.IntegerField()      # price after discount calculated in the backend

    rice=models.IntegerField()
    discount_rice=models.IntegerField()
    after_discount_rice=models.IntegerField()

    eggs=models.IntegerField()
    discount_eggs=models.IntegerField()
    after_discount_eggs=models.IntegerField()

    sugar=models.IntegerField()
    discount_sugar=models.IntegerField()
    after_discount_sugar=models.IntegerField()

    salt=models.IntegerField()
    discount_salt=models.IntegerField()
    after_discount_salt=models.IntegerField()

    vegetables=models.IntegerField()
    discount_vegetables=models.IntegerField()
    after_discount_vegetables=models.IntegerField()


    # FINDING THE INDIVIDUAL PRICE OF INGREDIENTS AFTER APPLYING THE DISCOUNT AMOUNT
    def save(self,*args,**kwargs):
        self.after_discount_flour=self.flour-self.discount_flour
        self.after_discount_rice=self.rice-self.discount_rice
        self.after_discount_eggs=self.eggs-self.discount_eggs
        self.after_discount_sugar=self.sugar-self.discount_sugar
        self.after_discount_salt=self.salt-self.discount_salt
        self.after_discount_vegetables=self.vegetables-self.discount_vegetables
        super(Stores,self).save(*args,**kwargs)


# TABLE FOR ALL RECIPES

class Recipe(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    ingredients=models.TextField()