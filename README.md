FastAlchemy
===========

[![codecov](https://codecov.io/gh/cloudeyes/fastalchemy/branch/master/graph/badge.svg)](https://codecov.io/gh/cloudeyes/fastalchemy)

SQLAlchemy Middleware for [FastAPI](http://github.com/tiangolo/fastapi) inspired by the [official tutorial](https://fastap.tiangolo.com/tutorial/sql-databases).


Features
--------

- Super-easy configuration: simply put `database.py` and `models.py` files in your project folder with the following code.

```python
from fastapi import FastAPI
from fastalchemy import SQLAlchemyMiddlware

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware)
```

Details
-------

Please peek `tests/app` folder if you want to know the way to create `database.py` and `models` py.
