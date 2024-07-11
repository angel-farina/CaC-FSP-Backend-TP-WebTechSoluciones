# corremos shell
python manage.py shell

# dentro de la shell corremos el siguiente codigo:
from contacts.models import UserCredentials
from django.contrib.auth.hashers import make_password

 <!-- Crear un nuevo usuario con contraseña encriptada -->
username = 'admin'
password = '1234'

hashed_password = make_password(password)
user = UserCredentials(username=username, password=hashed_password)
user.save()

print(f"Usuario {username} creado con contraseña {password} (encriptada: {hashed_password})")

# respuesta:
Usuario admin creado con contraseña 1234 (encriptada: pbkdf2_sha256$720000$ltZiJLvXwn8IHotdJsbYPD$umd30HBDBJhN0EsL7oLnihOum49mlSMawYMfvodofWM=)

# verificar el usuario:
user = UserCredentials.objects.get(username='admin')
print(f"Usuario: {user.username}, Contraseña: {user.password}")
