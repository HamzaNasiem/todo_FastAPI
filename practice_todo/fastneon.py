# # FastAPI, SQLModel, aur doosre zaroori libraries ka import kia gaya hai.

# from fastapi import FastAPI, Depends, HTTPException
# from sqlmodel import SQLModel, Session, create_engine, select, Field
# from practice_todo import settings
# from contextlib import asynccontextmanager
# from typing import Optional, Annotated


# # Todo model ko SQLModel ke saath define kia gaya hai jo database table ke taur par kaam karega.
# class Todo(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True,)
#     todo: str = Field(index=True)
#     status: bool = Field(default=False)

# # Database URL ko psycopg2 ke compatibility ke liye modify kia gaya hai.
# connectionString = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")


# # Database engine banaya gaya hai.
# engine = create_engine(connectionString, connect_args={"sslmode": "require"}, pool_recycle=500)


# # Database tables banane ke liye ek function hai.
# def db_create_and_tables():
#     SQLModel.metadata.create_all(engine)


# # FastAPI app ke lifespan events ko handle karne ke liye async context manager banaya gaya hai.
# @asynccontextmanager
# async def life_span(app: FastAPI):
#     print("Creating Tables...b")
#     db_create_and_tables()
#     yield 


# # FastAPI app ki instance banai gayi hai.
# app = FastAPI(lifespan = life_span, title="Hello World API with DB",)


# # Database session ko retrieve karne ke liye dependency function banaya gaya hai.
# def get_session():
#     with Session(engine) as session:
#         yield session


# # Root endpoint
# @app.get("/")
# def get_root():
#     return {"Message": "Hello Hamza.....!!!"}


# # Naya todo item ko add karne ka endpoint.
# @app.post("/todo/", response_model=Todo)
# def get_todos(todo: Todo, session: Annotated[Session, Depends(get_session)]):
#     session.add(todo)
#     session.commit()
#     session.refresh(todo)
#     return todo


# # Sabhi todo items ko retrieve karne ka endpoint.
# @app.get("/todo/", response_model=list[Todo])
# def read_todos(session: Annotated[Session, Depends(get_session)]):
#     todos = session.exec(select(Todo)).all()
#     return todos


# # Todo item ko ID ke zariye update karne ka endpoint.
# @app.put("/todo/{todo_id}", response_model=Todo)
# def update_todo(todo_id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
#     select_todo = select(Todo).where(Todo.id == todo_id)
#     selected_todo = session.exec(select_todo).first()
#     # selected_todo = session.exec(select(Todo).where(Todo.id == todo_id)).first()
#     if not selected_todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     selected_todo.status = todo.status
#     session.commit()
#     session.refresh(selected_todo)
#     return selected_todo


# # Todo item ko ID ke zariye delete karne ka endpoint.
# @app.delete("/todo/{todo_id}", response_model=Todo)
# def delete_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
#     selected_todo = session.exec(select(Todo).where(Todo.id == todo_id)).first()
#     if not selected_todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     session.delete(selected_todo)
#     session.commit()
#     return selected_todo

#___________________________________________________________________________
#___________________________________________________________________________
#___________________________________________________________________________



# FastAPI, SQLModel, aur doosre zaroori libraries ka import kia gaya hai.
from fastapi import FastAPI, Depends, HTTPException  # FastAPI framework se dependencies import ki gayi hai.
from sqlmodel import SQLModel, Session, create_engine, select, Field  # SQLModel library se dependencies import ki gayi hai.
from practice_todo import settings  # Project settings ko import kiya gaya hai.
from contextlib import asynccontextmanager  # async context manager ko import kiya gaya hai.
from typing import Optional, Annotated  # Optional aur Annotated types ko import kiya gaya hai.

# Todo model ko SQLModel ke saath define kia gaya hai jo database table ke taur par kaam karega.
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Todo item ka unique identifier hai, jo integer type hai aur optional hai.
    todo: str = Field(index=True)  # Todo ka description, jise index kiya gaya hai for better performance.
    status: bool = Field(default=False)  # Todo ka status, default value False hai (yani incomplete).

# Database URL ko psycopg2 ke compatibility(مطابقت) ke liye modify kia gaya hai.
connectionString = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")

# Database engine banaya gaya hai.
engine = create_engine(connectionString, connect_args={"sslmode": "require"}, pool_recycle=500)

# Database tables banane ke liye ek function hai.
def db_create_and_tables():
    SQLModel.metadata.create_all(engine)

# FastAPI app ke lifespan events ko handle karne ke liye async context manager banaya gaya hai.
@asynccontextmanager
async def life_span(app: FastAPI):
    print("Tables bana rahe hain...")  # Ek message print kia gaya hai lifespan ke event ke doran.
    db_create_and_tables()  # Database tables ko create kia gaya hai.
    yield 

# FastAPI app ki instance banai gayi hai.
app = FastAPI(lifespan=life_span, title="Hello World API with DB")

# Database session ko retrieve karne ke liye dependency function banaya gaya hai.
def get_session():
    with Session(engine) as session:
        yield session

# Root endpoint, jo sirf "Hello Hamza.....!!!" ka message return karta hai.
@app.get("/")
def get_root():
    return {"Message": "Hello Hamza.....!!!"}

# Naya todo item ko add karne ka endpoint.
@app.post("/todo/", response_model=Todo)
def get_todos(todo: Todo, session: Annotated[Session, Depends(get_session)]):
    session.add(todo)  # Naya todo item session me add kia gaya hai.
    session.commit()  # Session ko commit kia gaya hai.
    session.refresh(todo)  # Todo item ko refresh kia gaya hai taake sahi ID mil sake.
    return todo  # Added todo item ko return kia gaya hai.

# Sabhi todo items ko retrieve karne ka endpoint.
@app.get("/todo/", response_model=list[Todo])
def read_todos(session: Annotated[Session, Depends(get_session)]):
    todos = session.exec(select(Todo)).all()  # Sabhi todo items ko database se retrieve kia gaya hai.
    return todos  # Sabhi todo items ko return kia gaya hai.

# Todo item ko ID ke zariye update karne ka endpoint.
@app.put("/todo/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
    select_todo = select(Todo).where(Todo.id == todo_id)  # Di gayi ID ke corresponding todo item ko retrieve kia gaya hai.
    selected_todo = session.exec(select_todo).first()  # Selected todo item ko fetch kia gaya hai.
    if not selected_todo:  # Agar todo item nahi milta hai to 404 HTTP error throw kia jata hai.
        raise HTTPException(status_code=404, detail="Todo not found")
    selected_todo.status = todo.status  # Todo item ka status update kia gaya hai.
    session.commit()  # Session ko commit kia gaya hai.
    session.refresh(selected_todo)  # Updated todo item ko refresh kia gaya hai.
    return selected_todo  # Updated todo item ko return kia gaya hai.

# Todo item ko ID ke zariye delete karne ka endpoint.
@app.delete("/todo/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
    selected_todo = session.exec(select(Todo).where(Todo.id == todo_id)).first()  # Di gayi ID ke corresponding todo item ko retrieve kia gaya hai.
    if not selected_todo:  # Agar todo item nahi milta hai to 404 HTTP error throw kia jata hai.
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(selected_todo)  # Todo item ko database se delete kia gaya hai.
    session.commit()  # Session ko commit kia gaya hai.
    return selected_todo  # Deleted todo item ko return kia gaya hai.
