from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
import os
from dotenv import load_dotenv

# environment var
load_dotenv()

# db data from .env
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Engine and data
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
metadata = MetaData()

# Tables
article = Table('article', metadata,
                Column('id', Integer, primary_key=True),
                Column('title', String(255), nullable=False),
                Column('text', String, nullable=False))

comment = Table('comment', metadata,
                Column('id', Integer, primary_key=True),
                Column('article_id', Integer, ForeignKey('article.id'), nullable=False),
                Column('text', String, nullable=False))

connection = engine.connect()

# SQL query
query = select(article).outerjoin(comment, article.c.id == comment.c.article_id).where(comment.c.id.is_(None))

result = connection.execute(query)

# Print result
for row in result:
    print(f"ID: {row[0]}, Title: {row[1]}")

connection.close()
