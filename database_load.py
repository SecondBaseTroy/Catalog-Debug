from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import *
from database_config import Base, Category, CategoryItem
from sqlalchemy.orm import sessionmaker

print "creating link to database"
engine = create_engine('sqlite:///catalogshoes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear the database tables
print "clearing the database tables"
session.query(Category).delete()
session.query(CategoryItem).delete()

# Add categories
print "creating categories"
sample_categories = ['Mens Shoes', 'Womens Shoes', 'Baby Shoes']

for category_name in sample_categories:
    category = Category(category_name)
    session.add(category)
session.commit()

# Mens Shoes Items
print "creating items in categories"
item = CategoryItem("Running Shoes","Steve",
                    "Running shoes for active men.", 1)
session.add(item)
session.commit()

item = CategoryItem("Office Shoes","Mike",
                    "Shoes for the office.", 1)
session.add(item)
session.commit()

item = CategoryItem("Hiking Boots","Rob",
                    "Outdoor boots for all weather and all terrian.", 1)
session.add(item)
session.commit()

# Womens Shoes Items
item = CategoryItem("Dress Shoes","Suzanne",
                    "Dress shoes for office or a night out on the town.", 2)
session.add(item)
session.commit()

item = CategoryItem("Trainers","Laura",
                     "Great for working out or relaxing in.", 2)
session.add(item)
session.commit()

item = CategoryItem("Sandals","Carol",
                    "Great for the beach or going shopping with ladies.", 2)
session.add(item)
session.commit()

# Baby Shoes Category
item = CategoryItem("First Shoes","Riley",
                     "Great first picture shoes.", 3)
session.add(item)
session.commit()

item = CategoryItem("Baby Sandals","Katie",
                    "Something quick and easy to put on the baby.", 3)
session.add(item)
session.commit()
