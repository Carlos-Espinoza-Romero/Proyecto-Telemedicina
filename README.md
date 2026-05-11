# Pytest

## Instalación

```bash
pip install pytest pytest-django pytest-cov faker
```

## Configuración `pytest.ini`

```ini
[pytest]
DJANGO_SETTINGS_MODULE=django_telemedicina.settings
python_files=tests.py test_*.py *_tests.py
filterwarnings=ignore::DeprecationWarning
```

## Ejecución

```bash
pytest -v -rA -s
# -v: Muestra el nombre de cada test y su resultado
# -rA: Muestra un resumen detallado al final.
# -s: Desactiva la captura stdout. Permite ver los print() que tengan en el codigo.
```

## Despliegue

```env
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''

NUBEFACT_URL=''
NUBEFACT_TOKEN=''
```
