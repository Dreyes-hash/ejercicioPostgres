import orm.modelos as modelos
from sqlalchemy.orm import Session

def find_user_byid(session: Session, id_usuario:int):
    return session.query(modelos.Usuario).filter(modelos.Usuario.id == id_usuario).first()

def find_compra_byid(session: Session, id_compra:int):
    return session.query(modelos.Compra).filter(modelos.Compra.id == id_compra).first()

def find_foto_byid(session: Session, id_foto:int):
    return session.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()