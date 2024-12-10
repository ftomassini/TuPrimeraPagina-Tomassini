#Instalación
1. Clona este repositorio:

bash
git clone https://github.com/tu-usuario/TuPrimeraPaginaTomassini.git
cd TuPrimeraPaginaTomassini

2. Instala las dependencias necesarias:

bash
pip install -r requirements.txt

3. Realiza las migraciones de la base de datos:

bash
python manage.py makemigrations
python manage.py migrate

4. Crea un superusuario para el panel de administración:

bash
python manage.py createsuperuser

5. Inicia el servidor de desarrollo:

bash
python manage.py runserver
