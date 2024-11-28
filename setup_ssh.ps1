# Script pour gérer les clés SSH/GPG et leur configuration
$sshFolder = "$HOME\.ssh"
$gpgFolder = "$HOME\AppData\Roaming\gnupg"

# Vérifie si le dossier SSH existe, sinon le crée
if (!(Test-Path -Path $sshFolder)) {
    Write-Output "Création du dossier SSH..."
    New-Item -ItemType Directory -Path $sshFolder -Force
}

Function ListKeys {
    Write-Output "=== Liste des clés SSH existantes ==="
    Get-ChildItem -Path $sshFolder -Filter "id_*" | ForEach-Object { $_.Name }
    Write-Output "==============================="
}

Function DeleteAllKeys {
    Write-Output "Suppression de toutes les clés SSH..."
    Remove-Item -Path "$sshFolder\id_*" -Force -ErrorAction SilentlyContinue
    Write-Output "Suppression du fichier config SSH..."
    Remove-Item -Path "$sshFolder\config" -Force -ErrorAction SilentlyContinue
    Write-Output "Toutes les clés et le fichier config ont été supprimés."
}

Function DeleteSpecificKey {
    param (
        [string]$KeyName
    )
    $keyPath = "$sshFolder\$KeyName"
    if (Test-Path -Path $keyPath) {
        Write-Output "Suppression de la clé $KeyName..."
        Remove-Item -Path "$keyPath*" -Force
        Write-Output "Clé supprimée."
    } else {
        Write-Output "Clé $KeyName non trouvée."
    }
}

Function GenerateSSHKey {
    param (
        [string]$KeyType,
        [string]$KeyName
    )
    if ($KeyName -eq "") {
        $KeyName = "id_$KeyType"
    }
    $keyPath = "$sshFolder\$KeyName"
    Write-Output "Génération d'une clé SSH ($KeyType)..."
    ssh-keygen -t $KeyType -C "votre_email@example.com" -f $keyPath
    ssh-add $keyPath
    Write-Output "Clé SSH générée : $KeyName"
    Write-Output "Ajoutez la clé publique suivante à GitHub :"
    Get-Content "$keyPath.pub" | Set-Clipboard
    Get-Content "$keyPath.pub"
}

Function GenerateGPGKey {
    Write-Output "Génération d'une clé GPG pour GitHub..."
    $gpgConfig = @"
    %no-protection
    Key-Type: 1
    Key-Length: 4096
    Subkey-Type: 1
    Subkey-Length: 4096
    Name-Real: Votre Nom
    Name-Email: votre_email@example.com
    Expire-Date: 0
"@
    $gpgConfig | Out-File -FilePath "$gpgFolder\gpg_batch"
    gpg --batch --gen-key "$gpgFolder\gpg_batch"
    Write-Output "Clé GPG générée. Ajoutez-la à GitHub."
    gpg --armor --export "votre_email@example.com" | Set-Clipboard
    gpg --armor --export "votre_email@example.com"
}

Function UpdateConfig {
    param (
        [string]$KeyType,
        [string]$KeyName
    )
    $configPath = "$sshFolder\config"
    if (!(Test-Path -Path $configPath)) {
        Write-Output "Création d'un nouveau fichier config..."
    }
    $keyPath = "$sshFolder\$KeyName"
    $configContent = @"
Host github.com
  HostName github.com
  User git
  IdentityFile $keyPath
  IdentitiesOnly yes
"@
    $configContent | Out-File -FilePath $configPath -Append
    Write-Output "Fichier config mis à jour avec la clé $KeyName."
}

Function ViewEditConfig {
    Write-Output "=== Contenu actuel du fichier config ==="
    if (Test-Path -Path "$sshFolder\config") {
        Get-Content "$sshFolder\config"
    } else {
        Write-Output "Aucun fichier config trouvé."
    }
    Write-Output "Souhaitez-vous éditer le fichier ? (o/n)"
    $response = Read-Host
    if ($response -eq "o") {
        notepad "$sshFolder\config"
    }
}

# Menu principal
while ($true) {
    Write-Output "=== Menu de gestion des clés ==="
    Write-Output "1. Lister les clés existantes"
    Write-Output "2. Supprimer toutes les clés (et fichier config)"
    Write-Output "3. Supprimer une clé spécifique"
    Write-Output "4. Générer une clé SSH (ed25519 ou rsa)"
    Write-Output "5. Générer une clé GPG pour GitHub"
    Write-Output "6. Voir/Éditer le fichier config"
    Write-Output "7. Quitter"
    $choice = Read-Host "Choisissez une option"
    switch ($choice) {
        1 { ListKeys }
        2 {
            Write-Output "Êtes-vous sûr de vouloir supprimer toutes les clés ? (o/n)"
            $response = Read-Host
            if ($response -eq "o") {
                DeleteAllKeys
            } else {
                Write-Output "Action annulée."
            }
        }
        3 {
            Write-Output "Entrez le nom de la clé à supprimer (ex: id_rsa)"
            $keyName = Read-Host
            DeleteSpecificKey -KeyName $keyName
        }
        4 {
            Write-Output "Choisissez le type de clé à générer (ed25519 ou rsa)"
            $keyType = Read-Host
            Write-Output "Entrez un nom pour la clé (laisser vide pour un nom par défaut)"
            $keyName = Read-Host
            GenerateSSHKey -KeyType $keyType -KeyName $keyName
            UpdateConfig -KeyType $keyType -KeyName $keyName
        }
        5 { GenerateGPGKey }
        6 { ViewEditConfig }
        7 { break }
        default { Write-Output "Option invalide." }
    }
}
