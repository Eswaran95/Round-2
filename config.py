import os

NAME_DB = os.getenv('NAME_DB', 'postgres')
PORT_DB = os.getenv('PORT_DB', '5432')
PWD_DB = os.getenv(
  'PWD_DB',
  'postgres',
  )
HOST_DB = os.getenv(
  'HOST_DB',
  'localhost'
  )
USER_DB = os.getenv('USER_DB', 'postgres')

conString = "postgres://YourUserName:YourPassword@YourHost:5432/YourDatabase"

URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'

SCHEMAS = [
  "client1",
  "client2"
]

SELECTED_SCHEMA = os.getenv('SELECTED_SCHEMA', "client1")
