# from sqlmodel import Field, SQLModel, Relationship, Session, select, create_engine
# from typing import Optional, List
# import posts, users
# import os
# import dotenv

# dotenv.load_dotenv()
#
# # make a connection to the database
# conn_str = os.getenv("DATABASE_URL")
# engine = create_engine(conn_str, echo=True)
#
# # create the database
# SQLModel.metadata.create_all(engine)
#
# # create a session
# session = Session(engine)
#
# # create a user
# # user_1 = users.User(username="admin", email="admin@example", password="admin")
