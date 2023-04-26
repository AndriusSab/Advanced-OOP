from models import Vaikas, Tevas
from session import session

vaikas = Vaikas(
    vardas="Vaikas", pavarde="Tevaika", mokymo_istaiga="Čiurlionio gimnazija"
)

tevas = Tevas(vardas="Tevas", pavarde="Tevaika", vaikas=vaikas)
session.add(tevas)
session.commit()
