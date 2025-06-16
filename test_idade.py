def maior_de_idade(idade):
    return idade >= 18
def test_maior_de_idade():
    assert maior_de_idade(18)==True
    assert maior_de_idade(17)==False
    assert maior_de_idade(100)==True