
# 🎯 Django Models

## 🏆 Objective:
In this exercise, you’ll practice defining Django models, creating relationships between models, and working with migrations to update the database schema.

---

## 📝 Steps:

### 1. 🖥️ Define a Basic Model
- Create a model called `Author` with the following fields:
  - `first_name`: CharField (max_length=50)
  - `last_name`: CharField (max_length=50)
  - `birthdate`: DateField

- Create a model called `Book` with the following fields:
  - `title`: CharField (max_length=100)
  - `published_date`: DateField
  - `author`: ForeignKey (linking to the `Author` model)


### 2. 🧩 Work with Model Methods
- Add a method to the `Author` model that returns the full name of the author (i.e., first name + last name).
- Add a method to the `Book` model that checks if the book was published in the last 10 years.

---


Happy coding! 🚀📚