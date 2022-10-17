from Menu import Menu
from MenuRepository import MenuRepository
from UserInterface import UserInterface
from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
def test_check_user_input(monkeypatch):
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(3, "Test 2", 10)
    
    # Act
    menu_repository.set_menu_item(menu1)
    monkeypatch.setattr('builtins.input', lambda _: "3 2")
    pedido = user_interface.get_user_input()
    
    # Assert
    assert Order(3, 2) == pedido