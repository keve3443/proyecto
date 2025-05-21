import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "myproyecto-5c5c5",
  "private_key_id": "2693a4c096f554e5e35271eac13c66cb7b452104",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+oAfTC3KJp/qR\nLumSD8aMiW+LTqSwljseiYVMK8gKT+Iw4+bzx9p2WLs802Kclf7/8rky85jfBSb8\nDYU5+buQ8xq3QfjfxPgjRrelxUQxzZew5amOu1WztBEjPmy1vJdIFe8v5o9vVqPC\nNLbEDf7j2blyseUmDOaxT/DUI83h/suuXGX3PSPFNTNolHC+IEPIt44d/cMBr6BC\nvWCYnVoXgk9otQYg+SHvKlCUrya4N1GaG1fDr/55sUguonHcb/c+65ysGpAXwsmR\nJNFofg32xYYPc3VvkeL28vr+CyxuylDj11BAcqrYo70GH1Q4+QYfeAN64yvqCG7q\nJG6yIFRfAgMBAAECggEAH/tyhJ6Zj23u9LfVuUtLSR3v6IP/zp7N+XAiPKblz5Ea\nhpBeGc2QoiV9+JUQqOvjliavmtRS9CwFn+lWzmTPauDWvSNk8Yo3BZgiTL49lEuF\npUjK+2cD2HwgGfUpwQ4MpawEbtl0fD4hiH5Woasldi371rnxE8K7W8lpQvZk3wMa\nAslDyfEd7VvxlbWh/2QhtMmLxk2J5R0rvN5kPtRv7Vo0jd1y4F7RWTXrgyg5IITX\nK7/a4T2m5UNWrPp7m6aXlq0WRAa61+oHGsRFLiyJfEJ5zzi2kgutQTTHLEvtrbKh\nh2JQBoc1QP6ZFwpcRbpFafMGbWvp9tTMkxTLD15MyQKBgQDp5nlliSBBUm83SSIu\nHb2IUeFpx2iqhEj1QlHfW9V76K+BkITYMKcqRS5PJ5g3eMKcZHlL+EFOEno4rNQm\nKz0bFLGkGK/045uEEFO1ytWsZ+rd8awxM3PwNSwggRwK56n6jje4tufD5b4X7kGx\n+0rS7oFNWhkQ+9OkzRsPUTxCxwKBgQDQotOcQOCrBoaKwgtk+pn0nMTgcGUnJHkT\nd9rZe9AsdnW5S9e8dxu29kMvlNarPxWJh6fgEX/kOEXJvAH97SVT1FiEx2fioVyf\nUbs8RT/9zF3isJt9Nk1j+Di316C0jWTII0SAkrLfBzPfDRlPfmd0G9MpjRQ0ILj6\nB/UmDcbJqQKBgQCqtw3ZntkM9Da6OkWZNRm1mlWUl/d7pSt+3pXVGTjaxDz8qtda\n1z/bKT0ghryhmCEqdmbVnO9FJVVRcksxRJPH5TW2mFIswccq/6OpZs7Hk90nepF8\nI5q2MojvfGxURTuZ5R0kU1Mbdt5kpwAKAGhfRbbYFy9+Zt7VROJALsF11wKBgFPF\n/agRGOUzUpSmw8KBKY5h4F+qYcNszrz1dEe9gmJIEo8bl/2R6ev2SBXz8pqCUxiN\nAuhivnKZ8dPGDRqzvThC3GQ8WUdTuYgzXjYeLEqxY8VhWp3VTw/kHIodJ+c3mw8N\nsjTaMr6A+uAGN3KG8+1YOtrFTiZ8OSoURehIwdg5AoGBAIBiGzF67wfCX4x1ACju\nPb4LW7W+MDxz2yOn5L+qVigNWVrjVabfO6zafyrRkwWEFE05ToJzJnEWzSRE5r62\nIwc+v4+k9OvQ2Zw45T0Q3KhhqtOwf1K7X/sSkhKKIDVS1Y2Tzymg3kCYlSY9E4C7\nspYI5LYN5/ZN9onoAjpN8Ge+\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@myproyecto-5c5c5.iam.gserviceaccount.com",
  "client_id": "117185339571921268907",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40myproyecto-5c5c5.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproyecto-5c5c5-default-rtdb.firebaseio.com'
})
import time
import logging

logging.basicConfig(filename='listener.log', level=logging.ERROR)

MAX_REINTENTOS = 5
reintentos = 0

while reintentos < MAX_REINTENTOS:
    try:
        print("Iniciando listener...")
        raise ConnectionError("Error de conexión simulado")
    except (ConnectionError, TimeoutError) as e:
        reintentos += 1
        logging.error(f"Intento {reintentos}: Error de conexión detectado: {e}")
        print(f"Intento {reintentos}/{MAX_REINTENTOS}. Reiniciando en 5 segundos...")
        time.sleep(5)
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        print(f"Ocurrió un error inesperado: {e}. Reiniciando en 5 segundos...")
        time.sleep(5)

print("Se alcanzó el número máximo de reintentos. Terminando proceso.")
user_data = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "is_active": True,
    "roles": ["editor", "viewer"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    },
    "login_count": 15
}
ref = db.reference('/users')
new_user_ref = ref.push()
new_user_ref.set(user_data)
print(f"Nuevo usuario añadido con clave: {new_user_ref.key}")

user_id = "user123"
db.reference(f'users/{user_id}').set(user_data)
print(f"Datos de usuario con ID {user_id} establecidos.")
try:
    data = db.reference('/name').get()
    print(f"Valor en /name: {data}")
    user_id = "user123"
    user_data_read = db.reference(f'users/{user_id}').get()
    if user_data_read:
        print(f"Datos del usuario {user_id}: {user_data_read}")
    else:
        print(f"No se encontraron datos para el usuario {user_id}.")

except Exception as e:
    print(f"Error al leer datos: {e}")
user_id = "user123"
updates = {
    "name": "Jane Smith",
    "address/city": "Newville"
}
db.reference(f'users/{user_id}').update(updates)
print(f"Datos del usuario {user_id} actualizados.")
user_id = "user123"
db.reference(f'users/{user_id}/age').delete()
print(f"Campo 'age' eliminado para el usuario {user_id}.")
try:
    pushes_snapshot = pushes_snapshot = db.reference('/pushes').get()

    if pushes_snapshot:
        first_key = list(pushes_snapshot.keys())[0]

        print(f"Eliminando elemento con clave: {first_key}")
        db.reference(f'/pushes/{first_key}').delete()
        print("Elemento eliminado.")
    else:
        print("No hay elementos para eliminar en 'pushes'.")
except Exception as e:
    print(f"Error al eliminar elemento con clave push: {e}")