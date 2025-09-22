import pytest
from ast import PyCF_OPTIMIZED_AST
from scr.main import *
from unittest.mock import patch

@pytest.mark.asyncio
def teste_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def teste_funcaoteste():
    with patch('random.randint', return_value=25000):
        result = funcaoteste()
        yield result
    assert result == {"Teste": True, "num_aleatório" : 25000}

def teste_cadastrar_estudante(estudante: Estudante):
    estudante_teste = Estudante(nome="Gustavo", curso="ADS", ativo=True)
    result = cadastrar_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

def teste_atualizar_estudante_negativo():
    result = atualizar_estudante(-1)
    yield result
    assert not result

def teste_atualizar_estudante_positivo():
    result = atualizar_estudante(1)
    yield result
    assert result

def teste_deletar_estudante_negativo():
    result = deletar_estudante(-1)
    yield result
    assert not result

def teste_deletar_estudante_positivo():
    result = deletar_estudante(1)
    yield result
    assert result
