
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')



# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui

def heroi_existe(id_h):
    with engine.connect() as con:
        statement = text (""" SELECT * FROM heroi where id = :heroi""")
        resp = con.execute(statement, heroi = id_h)
        heroi = resp.fetchone()
        if heroi == None:
            return False
        return True


def consultar_heroi(id_h):
    with engine.connect() as con:
        statement = text (""" SELECT * FROM heroi where id = :heroi""")
        resp = con.execute(statement, heroi = id_h)
        heroi = resp.fetchone()
        if heroi == None:
            raise HeroiNaoExisteException
        return dict(heroi)