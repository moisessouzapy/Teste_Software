from DestinoRepository import DestinoRepository
from Destino import Destino


def test_adicionar_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino(61, "Brasília")
    destino2 = Destino(71, "Salvador")
    destino3 = Destino(31, "Belo Horizonte")
    # Act

    destino_repository.adicionar_destino(destino1)
    destino_repository.adicionar_destino(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 2
    assert not destino3 in destino_repository.lista_destino
    assert type(destino_repository.lista_destino) == list


def test_destino_existe():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino(21, "Rio de Janeiro")
    destino2 = Destino(71, "Salvador")
    destino_repository.adicionar_destino(destino1)

    # Act

    resultOK = destino_repository.checa_se_destino_existe(21)
    resultNOK = destino_repository.checa_se_destino_existe(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 1
    assert resultOK == True
    assert resultNOK == False