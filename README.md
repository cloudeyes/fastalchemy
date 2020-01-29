FastAlchemy
===========

SQLAlchemy Middleware for [FastAPI](http://github.com/tiangolo/fastapi) inspired by the [official tutorial](https://fastap.tiangolo.com/tutorial/sql-databases).


Features
--------

- Super-easy configuration: Just read put `database.py` and `models.py` in your project folder with the following code.

```python
from fastapi import FastAPI
from fastalchemy import SQLAlchemyMiddlware

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware)
```

Details
-------

Please peek `tests/app` folder if you want to know the way to create `database.py` and `models` py.
