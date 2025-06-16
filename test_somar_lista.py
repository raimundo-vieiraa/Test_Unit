def somar_lista(lista):
    return sum(lista)
def test_somar_lista():
    assert somar_lista([1,2,2,5])==10
    assert somar_lista([])==0
    assert somar_lista([5,-5])==0