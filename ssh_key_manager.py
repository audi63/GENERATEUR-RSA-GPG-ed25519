import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget,
    QFileDialog, QMessageBox
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize


class SSHKeyManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionnaire de Clés SSH et GPG")
        self.setMinimumSize(800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2f33; /* Dark background */
                color: #ffffff;          /* White text */
            }
            QPushButton {
                background-color: #3f51b5; /* Modern blue */
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                transition: background-color 0.3s ease; /* Smooth hover effect */
            }
            QPushButton:hover {
                background-color: #5c6bc0; /* Lighter blue on hover */
            }
            QPushButton:pressed {
                background-color: #283593; /* Darker blue when pressed */
            }
            QLabel {
                font-size: 20px;
                font-weight: bold;
                margin: 20px;
            }
        """)
        # Initialiser les widgets
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Titre principal
        title_label = QLabel("Gestionnaire de Clés SSH et GPG")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Ajouter les boutons avec icônes
        buttons = [
            ("Lister les clés existantes", "icons/list.svg", self.list_keys),
            ("Supprimer toutes les clés", "icons/delete_all.svg", self.delete_all_keys),
            ("Supprimer une clé spécifique", "icons/delete.svg", self.delete_specific_key),
            ("Générer une clé SSH (ED25519 ou RSA)", "icons/key.svg", self.generate_ssh_key),
            ("Générer une clé GPG pour GitHub", "icons/gpg.svg", self.generate_gpg_key),
            ("Voir/Éditer le fichier config", "icons/edit.svg", self.view_edit_config),
            ("Quitter", "icons/exit.svg", self.close),
        ]

        for text, icon_path, callback in buttons:
            button = QPushButton(text)
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(24, 24))  # Utilisation correcte de QSize
            button.clicked.connect(callback)
            layout.addWidget(button)

        # Définir le layout central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def list_keys(self):
        """Lister les clés existantes dans ~/.ssh"""
        ssh_folder = os.path.expanduser("~/.ssh")
        if not os.path.exists(ssh_folder):
            QMessageBox.information(self, "Aucune clé", "Aucune clé SSH n'a été trouvée.")
            return

        keys = [f for f in os.listdir(ssh_folder) if f.startswith("id_")]
        if keys:
            QMessageBox.information(self, "Clés SSH existantes", "\n".join(keys))
        else:
            QMessageBox.information(self, "Aucune clé", "Aucune clé SSH n'a été trouvée.")

    def delete_all_keys(self):
        """Supprimer toutes les clés SSH et le fichier config"""
        ssh_folder = os.path.expanduser("~/.ssh")
        if not os.path.exists(ssh_folder):
            QMessageBox.warning(self, "Erreur", "Le dossier ~/.ssh n'existe pas.")
            return

        confirm = QMessageBox.question(
            self, "Confirmation", "Voulez-vous supprimer toutes les clés SSH et le fichier config ?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            for file in os.listdir(ssh_folder):
                if file.startswith("id_") or file == "config":
                    os.remove(os.path.join(ssh_folder, file))
            QMessageBox.information(self, "Succès", "Toutes les clés SSH ont été supprimées.")

    def delete_specific_key(self):
        """Supprimer une clé spécifique"""
        ssh_folder = os.path.expanduser("~/.ssh")
        key_path, _ = QFileDialog.getOpenFileName(self, "Sélectionnez une clé", ssh_folder)
        if key_path and os.path.exists(key_path):
            os.remove(key_path)
            QMessageBox.information(self, "Succès", f"Clé supprimée : {key_path}")
        else:
            QMessageBox.warning(self, "Erreur", "Aucune clé n'a été supprimée.")

    def generate_ssh_key(self):
        """Générer une clé SSH"""
        ssh_folder = os.path.expanduser("~/.ssh")
        if not os.path.exists(ssh_folder):
            os.makedirs(ssh_folder)

        key_path, _ = QFileDialog.getSaveFileName(self, "Nom de la clé", os.path.join(ssh_folder, "id_ed25519"))
        if not key_path:
            return

        passphrase, ok = QFileDialog.getText(self, "Paraphrase", "Entrez une paraphrase pour protéger la clé (laisser vide pour aucune) :")
        if ok:
            cmd = ["ssh-keygen", "-t", "ed25519", "-f", key_path, "-N", passphrase]
            subprocess.run(cmd)
            QMessageBox.information(self, "Succès", f"Clé SSH générée : {key_path}")

    def generate_gpg_key(self):
        """Générer une clé GPG"""
        QMessageBox.information(self, "Non implémenté", "La génération de clé GPG n'est pas encore implémentée.")

    def view_edit_config(self):
        """Ouvrir le fichier config SSH dans VS Code"""
        config_path = os.path.expanduser("~/.ssh/config")
        if not os.path.exists(config_path):
            with open(config_path, "w") as file:
                file.write("# Configuration SSH\n")
        try:
            subprocess.run(["code", config_path], check=True)
        except FileNotFoundError:
            QMessageBox.warning(self, "Erreur", "Impossible d'ouvrir le fichier dans VS Code. Vérifiez votre installation.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SSHKeyManager()
    window.show()
    sys.exit(app.exec())
