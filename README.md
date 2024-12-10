# Instalación
1. Clona este repositorio:

`git clone https://github.com/tu-usuario/TuPrimeraPaginaTomassini.git`
`cd TuPrimeraPaginaTomassini`

2. Instala las dependencias necesarias:

`pip install -r requirements.txt`

3. Realiza las migraciones de la base de datos:

`python manage.py makemigrations`
`python manage.py migrate`

4. Crea un superusuario para el panel de administración:

`python manage.py createsuperuser`

5. Inicia el servidor de desarrollo:

`python manage.py runserver`

6. Ingresa a la web:

Ingresa al navegador a la dirección: http://127.0.0.1:8000/

7. Ingresar al panel admin:

Ingresa al navegador a la dirección: http://127.0.0.1:8000/admin
