# tests/test_cli.py

from click.testing import CliRunner
from monedero import cli


runner = CliRunner()

def test_app():
  result = runner.invoke(cli.app, ['-v'])
  assert result.exit_code == 0
  assert result.output == 'Monedero v0.2\n'

def test_get_coin():
    result = runner.invoke(cli.get, ['-c', 'coso'])
    assert result.exit_code == 0
    assert result.output == 'coso 2024-01-01\n'

def test_get_date():
    result = runner.invoke(cli.get, ['-c', 'coso', '-d', '2024-01-01'])
    assert result.exit_code == 0
    assert result.output == 'coso 2024-01-01\n'


def test_get_ambos():
    result = runner.invoke(cli.get, ['--coin', 'sebicoin', '-d', 'ayer'])
    assert result.exit_code == 0
    assert result.output == 'sebicoin ayer\n'

if __name__ == '__main__':
    test_app()
    test_get_coin()
    test_get_date()
    test_get_ambos()
