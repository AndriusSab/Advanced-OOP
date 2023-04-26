import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()


class Projektas(Base):
    __tablename__ = "Projektas"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)

# CRUD(CRUD – create, read, update, delete)
# Kaip sukurti ryšį su sukurta DB kitame faile:


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projektas import Projektas

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()


# Kaip įrašyti duomenis į lentelę:
projektas1 = Projektas("Naujas pr.", 20000)
session.add(projektas1)
session.commit()

projektas2 = Projektas("2 projektas", 55000)
session.add(projektas2)
session.commit()

# Kaip gauti duomenis iš lentelės (cRud):
projektas1 = session.query(Projektas).get(1)

print(projektas1.name)
# Naujas pr.
projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)

# Kaip ieškoti duomenų pagal sąlygą ar šabloną:

search = session.query(Projektas).filter(Projektas.name.ilike("2%"))
search2 = session.query(Projektas).filter(Projektas.price > 1000)
search3 = session.query(Projektas).filter(
    Projektas.price > 1000, Projektas.name.ilike("2%")
)

print([i for i in search])
print([i for i in search2])
print([i for i in search3])

# Kaip pakeisti duomenis lentelėje (crUd):
projektas1 = session.query(Projektas).get(1)
projektas1.price = 22000
session.commit()
projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
projektas2.name = "2 projektas tikrai"
session.commit()
