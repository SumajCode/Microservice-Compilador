# Compiler Microservice

Microservicio RESTful desarrollado en Flask para la compilación y evaluación de código fuente. Permite enviar código y entradas para su ejecución segura en un entorno sandbox, soportando principalmente Python.

---

# Entorno de deploy

URL deploy de servicio de docente
```
https://[microservicecompilador.onrender.com/apicompilador/v1](https://microservicecompilador.onrender.com/apicompilador/v1)
```

---

## 🚀 Características

- Compilación y evaluación de código fuente vía API
- Arquitectura modular y escalable
- Sandbox para ejecución segura
- Controladores y rutas desacopladas
- Configuración por variables de entorno
- Migraciones automáticas de base de datos (si aplica)
- Entorno virtual recomendado

---

## 📁 Estructura del Proyecto

```
compiler/
├── README.md
├── __init__.py
├── src/
│   ├── main.py
│   ├── config/
│   ├── domain/
│   ├── features/
│   │   └── sandbox/
│   │       └── SandBoxCompilerOnlyPython.py
│   ├── hooks/
│   ├── infra/
│   │   ├── controllers/
│   │   │   └── CodeController.py
│   │   └── routes/
│   │       ├── apigs.py
│   │       └── CodeRoutes.py
│   ├── scripts/
│   └── shared/
├── requirements.txt
└── .env
```

---

## ⚙️ Instalación y Configuración

### 1. Clona el repositorio y navega al directorio del proyecto

```bash
git clone https://github.com/SumajCode/Microservice-Compilador.git
cd /Microservice-Compiler
```

### 2. Crea y activa un entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Crea un archivo `.env` en la raíz de `compiler/` con, por ejemplo:

```env
FLASK_APP=src/main.py
FLASK_DEBUG=1
APP_NAME=CompilerMicroservice
APP_VERSION=1.0.0
HOST=localhost
PORT_API=4005
```

---

## 🏃‍♂️ Ejecución del Servidor

Todos los comandos deben ejecutarse desde el directorio `src`:

```bash
cd src
flask run
```

La aplicación estará disponible en: [http://localhost:4005](http://localhost:4005) (o el puerto configurado).

---

## 🛣️ Visualizar Rutas Disponibles

```bash
cd src
flask routes
```

---

## 📦 Dependencias Principales

- Flask
- Flask-CORS
- python-dotenv
- (y otras listadas en `requirements.txt`)

---

## 🧩 Ejemplo de Código

### main.py

```python
from infra.routes.apigs import createApp

application = createApp()

if __name__ == '__main__':
    application.run()
```

### apigs.py

```python
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from infra.routes.CodeRoutes import blueprint as blueCode

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    padreBlueprint = Blueprint('apicompilador', __name__, url_prefix='/apicompilador/v1')
    # ...rutas y blueprints...
    app.register_blueprint(padreBlueprint)
    return app
```

---

## 📚 Endpoints Principales

### Código

- `POST /apicompilador/v1/code/compilar` — Compila y ejecuta código fuente
- `POST /apicompilador/v1/code/evaluar` — Evalúa código fuente con pruebas con un solo argumento

#### Ejemplo de request para `/code/compilar`:

```json
POST /apicompilador/v1/code/compilar
Content-Type: application/json

{
  "lang": "python",
  "code": "print('Hola mundo')"
}
```

#### Ejemplo de request para `/code/evaluar`:

```json
POST /apicompilador/v1/code/evaluar
Content-Type: application/json

{
  "code":"\ndef suma(a:int, b: int=3):\n  return a+b",
  "lang":"python",
  "outputs":[5,4,8],
  "inputs":[2,2,5],
  "rules":{
        "functions":{
            "functionNames":["suma"]
        }
    },
  "functionInvoke":"suma"
}
```

---

## 📝 Notas

- Siempre activa el entorno virtual antes de instalar dependencias o ejecutar la aplicación.
- Usa variables de entorno para evitar exponer información sensible.
- El archivo de configuración `conf.py` centraliza la lectura de variables de entorno.
- El endpoint `/code/compilar` ejecuta el código en un entorno sandbox para mayor seguridad.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias o mejoras.
