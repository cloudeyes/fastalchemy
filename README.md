FastAlchemy
===========

[![Build Status](https://travis-ci.com/cloudeyes/fastalchemy.svg?branch=master)](https://travis-ci.com/cloudeyes/fastalchemy)
[![codecov](https://codecov.io/gh/cloudeyes/fastalchemy/branch/master/graph/badge.svg)](https://codecov.io/gh/cloudeyes/fastalchemy)

SQLAlchemy Middleware for [FastAPI](http://github.com/tiangolo/fastapi) inspired by the [official tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases).


Features
--------

- Super-easy configuration: simply put `database.py` and `models.py` files in your project folder with the following code.

```python
from fastapi import FastAPI
from fastalchemy import SQLAlchemyMiddlware, db

from models import User

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware)

@app.get('/users')
def get_users():
    return db.query(User).order_by(User.id).all()
```

Details
-------

Please peek `tests/app` folder if you want to know the way to create `database.py` and `models` py.
