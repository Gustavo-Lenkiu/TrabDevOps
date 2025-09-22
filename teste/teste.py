from scr.main import *
from unittest.mock import patch

def teste_root():
    assert root()== {"message": "Hello World"}

def teste_funcaoteste():
    with patch('random.randint', return_value=25000):
        result = funcaoteste()
    assert result == {"Teste": True, "num_aleatório" : 25000}

def teste_cadastrar_estudante(estudante: Estudante):
    estudante_teste = Estudante(nome="Gustavo", curso="ADS", ativo=True)
    assert estudante_teste == cadastrar_estudante()

def teste_atualizar_estudante_negativo():
    assert not atualizar_estudante(-1)

def teste_atualizar_estudante_positivo():
    assert atualizar_estudante(1)

def teste_deletar_estudante_negativo():
    assert not deletar_estudante(-1)

def teste_deletar_estudante_positivo():
    assert deletar_estudante(1)
