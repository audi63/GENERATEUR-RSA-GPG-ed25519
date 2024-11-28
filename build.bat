@echo off
:: Mise à jour de pip
python -m pip install --upgrade pip

:: Création de l'environnement virtuel
python -m venv venv
call venv\Scripts\activate

:: Installation des dépendances
pip install -r requirements.txt

:: Construction de l'exécutable avec PyInstaller
pyinstaller --onefile --noconsole --icon=icons/icon.ico ssh_key_manager.py

:: Message final
echo Build terminé. Consultez le dossier dist.
pause
