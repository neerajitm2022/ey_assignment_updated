#from app.controllers.addition_controller import perform_addition
from app.controllers.addition_controller import perform_addition
def test_perform_addition():
    numbers = [1, 2, 3, 4]
    assert perform_addition(numbers) == 10
