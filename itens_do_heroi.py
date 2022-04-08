from sqlalchemy import create_engine
from sqlalchemy.sql import text


class ItemNaoExisteException(Exception):
    pass

engine = create_engine('sqlite:///rpg.db')

def  heroi_tem_item(id_heroi):
    with engine.connect() as con:
        query = text (""" 
                      SELECT * from Heroi h 
                      join ItemDoHeroi itdh on itdh.idHeroi = h.id
                      join Item it on it.id = itdh.idItem
                      WHERE h.id = :heroi""")
        resp = con.execute(query, heroi = id_heroi)
        itens_heroi = resp.fetchone()
        if itens_heroi == None:
            return False
        return True

def heroi_quantos_itens(id_heroi):
    with engine.connect() as con:
        query = text (""" 
                      SELECT * from Heroi h 
                      join ItemDoHeroi itdh on itdh.idHeroi = h.id
                      join Item it on it.id = itdh.idItem
                      WHERE h.id = :heroi""")
        resp = con.execute(query, heroi = id_heroi)
        itens_heroi = resp.fetchall()
        return len(itens_heroi)

def itens_do_heroi(id_heroi):
    with engine.connect() as con:
        query = text (""" 
                      SELECT * from Heroi h 
                      join ItemDoHeroi itdh on itdh.idHeroi = h.id
                      join Item it on it.id = itdh.idItem
                      WHERE h.id = :heroi""")
        resp = con.execute(query, heroi = id_heroi)
        itens_heroi = resp.fetchall()
        return itens_heroi
        
        
