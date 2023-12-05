![Hbnb](https://i.ibb.co/tzWhF53/65f4a1dd9c51265f49d0.png)

# HolbertonBnB
## Cloning of AirBnB Website

The goal of the project is to deploy on your server a simple copy of the AirBnB website
A complete web application composed by:
  - A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
  - A website (the front-end) that shows the final product to everybody: static and dynamic
  - An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

# Steps
## Each step will link to a concept:


# The console

  - create your data model
  - manage (create, update, destroy, etc) objects via a console / command interpreter
  - store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![img](https://i.ibb.co/287QnyQ/815046647d23428a14ca.png)


# Web static

  - learn HTML/CSS
  - create the HTML of your application
  - create template of each object

![img](https://i.ibb.co/k4PN9jC/87c01524ada6080f40fc.png)


# MySQL storage

  - replace the file storage by a Database storage
  - map your models to a table in database by using an O.R.M.

![img](https://i.ibb.co/sqqFdgb/5284383714459fa68841.png)


# Web framework - templating

  - create your first web server in Python
  - make your static HTML file dynamic by using objects stored in a file or database

![img](https://i.ibb.co/YWxd2hz/cb778ec8a13acecb53ef.png)


# RESTful API

  - expose all your objects stored via a JSON web interface
  - manipulate your objects via a RESTful API

![img](https://i.ibb.co/SyyCv5S/06fccc41df40ab8f9d49.png)


# Web dynamic

  - learn JQuery
  - load objects from the client side by using your own RESTful API

![img](https://i.ibb.co/4PSRhvD/d2d06462824fab5846f3.png)


# Files and Directories

  - models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
  - tests directory will contain all unit tests.
  - console.py file is the entry point of our command interpreter.
  - models/base_model.py file is the base class of all our models. It contains common elements: 
    - attributes: id, created_at and updated_at
    - methods: save() and to_json()
  - models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.


# Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

  - Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
  - Provide default value of any attribute
  - In the future, provide the same model behavior for file storage or database storage


