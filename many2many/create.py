from models import Vaikas, Tevas
from session import session

tevas1 = Tevas(vardas="Tėvas", pavarde="Tėvaika")
tevas2 = Tevas(vardas="Motina", pavarde="Tevienė")
tevas3 = Tevas(vardas="Motina", pavarde="lala")
vaikas1 = Vaikas(vardas="Vaikas", pavarde="Tėvaika")
vaikas2 = Vaikas(vardas="Vaikė", pavarde="Tėvaikytė")

tevas1.vaikai.append(vaikas1)
tevas2.vaikai.append(vaikas1)
tevas3.vaikai.append(vaikas2)
tevas2.vaikai.append(vaikas2)

session.add(tevas1)
session.add(tevas2)
session.commit()
