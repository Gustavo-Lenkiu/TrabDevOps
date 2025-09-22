import pytest
from ast import PyCF_OPTIMIZED_AST
from scr.main import *
from unittest.mock import patch

@pytest.mark.asyncio
async def teste_root():
    result = await root()
    assert result == {"message": "Hello World"}

async def teste_funcaoteste():
    with patch('random.randint', return_value=25000):
        result = await funcaoteste()
    assert result == {"Teste": True, "num_aleatório" : 25000}

async def teste_cadastrar_estudante():
    estudante_teste = Estudante(nome="Gustavo", curso="ADS", ativo=True)
    result = await cadastrar_estudante(estudante_teste)
    assert estudante_teste == result

async def teste_atualizar_estudante_negativo():
    result = await atualizar_estudante(-1)
    assert not result

async def teste_atualizar_estudante_positivo():
    result = await atualizar_estudante(1)
    assert result

async def teste_deletar_estudante_negativo():
    result = await deletar_estudante(-1)
    assert not result

async def teste_deletar_estudante_positivo():
    result = await deletar_estudante(1)
    assert result
