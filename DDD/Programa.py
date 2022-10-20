from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()
destino_repository.adicionar_destino(Destino(61, "Brasília"))
destino_repository.adicionar_destino(Destino(71, "Salvador"))
destino_repository.adicionar_destino(Destino(21, "Rio de Janeiro"))
destino_repository.adicionar_destino(Destino(27, "Vitória"))
destino_repository.adicionar_destino(Destino(31, "Belo Horizonte"))

user_interface = InterfaceUsuario(destino_repository)

while user_interface.saida_usuario():
    pass