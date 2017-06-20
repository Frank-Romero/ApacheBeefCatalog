from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, User, MenuItem

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')

# Bind engine to metadata of the Base class.
Base.metadata.bind = engine

DBSDession = sessionmaker(bind=engine)
session = DBSDession()

# Create dummy user.
User1 = User(name="Butcher Man", email="meat@butcherman.com", picture="https://thumbs.dreamstime.com/x/butcher-cartoon-set-meat-sausage-knife-isolated-vector-illustration-84977087.jpg")
session.add(User1)
session.commit()

# Category for American Cuts
category1 = Category(user_id=1, name="American Cuts", description="The American primal cuts.")

session.add(category1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Brisket", description="From the breast, very tough and needs to be cooked for a long time.", category=category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Shank", description="From the leg, the toughest cut used in soups, stocks and very lean ground beef.", category=category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Plate", description=
					 "From the belly, it is cheap and tough, typically used for bacon, pastrami, ground beef and skirt/hanger steaks.", category=category1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Rib", description="As the name suggests, used as short ribs, prime rib, and rib eye steaks.", category=category1)

session.add(menuItem4)
session.commit()


# Category for Argentinian Cuts
category2 = Category(user_id=1, name="Argentinian Cuts", description="The most important cuts of beef in the Argentine cuisine.")

session.add(category2)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Asado", description="The large section of rib cage, including short and spare ribs.", category=category2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Bife de costilla", description="Porterhouse and T-bone steaks.", category=category2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Bola de lomo", description="The best part of the loin, the most tender and flavorful.", category=category2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Rinones", description="The kidneys.", category=category2)

session.add(menuItem4)
session.commit()


# Category for Brasilian Cuts.
category3 = Category(user_id=1, name="Brasilian Cuts", description="The most important cuts of beef in Brasilian cuisine.")

session.add(category3)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Acem", description="The arm/shoulder blade of the cow.", category=category3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Alcatra", description="Top sirloin, which is very flavorful.", category=category3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Lagarto", description="The outer round, or rump, of the cow.", category=category3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Cupim", description="The hump of the zebu cow.", category=category3)

session.add(menuItem4)
session.commit()


# Category for Beef Sausages
category4 = Category(user_id=1, name="Beef Sausages", description="The finest beef sausages.")

session.add(category4)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Bangers", description="UK sausage of minced beef mixed with cereals.", category=category4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Blood and Tonge Sausage", description="Beef tongues minced and mixed with gelatin, blood and spices.", category=category4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Bratwurst", description="Minced veal, or baby cow, mixed with pepper, sage and nutmeg.", category=category4)

session.add(menuItem3)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Lebanon Bologna", description="Dry sausage from Lebanon, PA; made of coarsely chopped beef and heavily smoked.", category=category4)

session.add(menuItem4)
session.commit()


print "Beefed!!!"
