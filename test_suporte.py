import pytest

from suporte import Suporte

def test_sem_chamado():
    suporte = Suporte("Chamados", 0)
    assert suporte.chamado_aberto == 0

def test_abrir_chamado():
    suporte = Suporte("Chamados", 0)
    suporte.abrir_chamado()
    assert suporte.chamado_aberto == 1

def test_fechar_chamado():
    suporte = Suporte("Chamados", 1)
    suporte.fechar_chamado()
    assert suporte.chamado_aberto == 0
