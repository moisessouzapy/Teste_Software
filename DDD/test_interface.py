from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario
from Destino import Destino

def solicitar_input_usuario(monkeypatch):
    # Arrange
    destino_repository = DestinoRepository()
    user_interface = InterfaceUsuario(destino_repository)

    # Act
    monkeypatch.setattr('builtins.input', lambda _: "11")
    destino1 = user_interface.solicitar_input_usuario()

    # Assert
    assert destino1 == 1

def test_saida_usuario(monkeypatch):
    #Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    user_interface = InterfaceUsuario(destino_repository)
    destino_repository.adicionar_destino(Destino(71, "Salvador"))

    # Act
    monkeypatch.setattr('builtins.input', lambda _: "71")
    destinoOK = user_interface.saida_usuario()

    monkeypatch.setattr('builtins.input', lambda _: "31")
    destinoNOK = user_interface.saida_usuario()

    # Assert
    assert destinoOK == True
    assert destinoNOK == False
