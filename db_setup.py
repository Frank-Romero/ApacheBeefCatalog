import os,sys
from sqlalchemy import Column, create_engine, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250), nullable=True)
	
	@property
	def serialize(self):
		return {
		'id':self.id,
		'name':self.name,
		'email':self.email
		}
		
class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	description = Column(String(250))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
		}

class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	description = Column(String(250))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category, backref=backref('menu_item', cascade='all, delete'))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'id':self.id,
			'name': self.name,
			'description': self.description,
			'category_id': self.category_id

		}

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
Base.metadata.create_all(engine)