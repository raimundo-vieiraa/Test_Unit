def fatorial(n):
    if n < 0:
        raise ValueError("Número não pode ser negativo")
    if n == 0:
        return 1
    return n * fatorial(n - 1)
def test_fatorial():
    assert fatorial(0)==1
    assert fatorial(5)==120
    try:
        fatorial(-1)
    except ValueError:
        assert True