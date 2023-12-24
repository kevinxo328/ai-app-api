from sqlalchemy import Boolean, Column, Integer, String

import utils.sql as sql_utils


class User(sql_utils.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String)

    # def __repr__(self):
    #     return "<User(id='%s', username='%s', hashed_password='%s')>" % (
    #         self.id,
    #         self.username,
    #         self.hashed_password,
    #     )

    # def __str__(self):
    #     return "User(id='%s', username='%s', hashed_password='%s')" % (
    #         self.id,
    #         self.username,
    #         self.hashed_password,
    #     )

    # def __init__(self, username, hashed_password):
    #     self.username = username
    #     self.hashed_password = hashed_password

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "hashed_password": self.hashed_password,
    #     }

    # def to_json(self):
    #     return json.dumps(self.to_dict())

    # def save(self):
    #     sql_utils.session.add(self)
    #     sql_utils.session.commit()

    # def delete(self):
    #     sql_utils.session.delete(self)
    #     sql_utils.session.commit()

    # @staticmethod
    # def get_all():
    #     return sql_utils.session.query(User).all()

    # @staticmethod
    # def get_by_id(id):
    #     return sql_utils.session.query(User).filter(User.id == id).first()

    # @staticmethod
    # def get_by_username(username):
    #     return sql_utils.session.query(User).filter(User.username == username).first()

    # @staticmethod
    # def get_by_username_and_password(username, password):
    #     return (
    #         sql_utils.session.query(User)
    #         .filter(User.username == username)
    #         .filter(User.hashed_password == password)
    #         .first()
    #     )
