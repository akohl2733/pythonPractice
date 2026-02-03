from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# create engine object for interacting with database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# return hello world
with engine.connect() as conn:
    result = conn.execute(text("select 'Hello World'"))
    print(result.all())

# use SQL text to create table, insert values, and commit changes
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y, int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{'x': 1, "y": 1}, {"x": 2, "y": 2}],
    )
    conn.commit()

# remove need for commit() method via 'begin once' style
with engine.begin() as conn:
    conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
        )
    
# fetch rows from db
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

# tuple version
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for x, y in result:  # see this line
        print(f"x: {x}, y: {y}")

# indexed version
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row[0]}, y: {row[1]}")

# using sqlalchemy.orm and Session
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

# using Session and .execute() for update
with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()