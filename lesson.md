# Leçon #1: Hardcoded Secrets 🔐

## 📝 Résumé de la Vulnérabilité

Les **secrets en dur** (hardcoded secrets) sont des credentials, clés API, ou tokens stockés directement dans le code source ou les fichiers de configuration. C'est l'une des vulnérabilités les plus critiques en sécurité informatique.

---

## 🚨 Qu'est-ce qui rend le code vulnérable?

### 1. **Secrets visibles dans le code source**
```python
# ❌ VULNÉRABLE
password = "SuperSecretPassword123!"
api_key = "sk-1234567890abcdefghijk"
```

### 2. **Stockage dans le contrôle de version Git**
```bash
# Si vous avez commit un .env ou un config.py avec secrets:
git log --all --full-history -- config.py
# Les secrets resteront dans l'historique Git POUR TOUJOURS!
```

### 3. **Exposition dans les logs de debug**
```python
# ❌ VULNÉRABLE
print(f"Database URL: {connection_string}")  # Contient le password!
logger.debug(f"API Key: {api_key}")
```

### 4. **Accessibilité aux développeurs non-autorisés**
- Tous les devs dans le repo ont accès aux secrets
- Anciens employés conservent l'accès à l'historique Git
- Risque de fuite si le repo est clone sans sécurité

### 5. **Pas de rotation possible**
- Pour changer un secret, il faut modifier le code
- Redeployer l'application complète
- Laisser des traces dans le contrôle de version

---

## 💥 Conséquences de la Vulnérabilité

### Risques Directs
- 🔴 **Accès non autorisé** à la base de données
- 🔴 **Vol de données** sensibles
- 🔴 **Manipulation de données** critiques
- 🔴 **Accès aux services externes** (AWS, APIs, etc.)
- 🔴 **Usurpation d'identité** (tokens compromis)
- 🔴 **Accès à toute l'infrastructure** (effet domino)

### Risques Indirects
- 🟠 **Perte de confiance** des clients
- 🟠 **Conformité** (GDPR, HIPAA, etc.)
- 🟠 **Responsabilité légale** et financière
- 🟠 **Couverture d'assurance** révoquée

### Exemple d'Attack Chain
```
1. Un dev fork le repo pour usage personnel
2. Le fork devient public accidentellement sur GitHub
3. Un acteur malveillant scanne les repos publics
4. Trouve les secrets hardcodés
5. Se connecte à la production
6. Vol de données utilisateurs
7. Chantage / Données vendues au dark web
8. Entreprise ruinée
```

---

## ✅ Solution: Bonnes Pratiques

### 1. **Utiliser les Variables d'Environnement**

```python
# ✅ SÉCURISÉ
import os

password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

if not password or not api_key:
    raise ValueError("Secrets manquants dans l'environnement")
```

### 2. **Fichier .env pour le Développement**

```bash
# .env (NE JAMAIS COMMIT)
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=app_user
DB_PASSWORD=dev_password_12345
API_KEY=sk-dev-key-only
JWT_SECRET=dev-secret-key
```

```bash
# .gitignore
.env
.env.local
.env.*.local
secrets/
config/*.key
```

### 3. **Charger avec python-dotenv**

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

# Charger le fichier .env
load_dotenv()

# Utiliser les variables
db_password = os.getenv("DB_PASSWORD")
```

### 4. **En Production: Gestionnaires de Secrets**

#### AWS Secrets Manager
```python
import boto3

client = boto3.client('secretsmanager')
secret = client.get_secret_value(SecretId='prod/db-password')
password = secret['SecretString']
```

#### HashiCorp Vault
```python
import hvac

client = hvac.Client(url='https://vault.example.com')
secret = client.secrets.kv.read_secret_version(path='prod/database')
password = secret['data']['data']['password']
```

#### Kubernetes Secrets
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  db-password: "secure-password-here"
```

```python
import os

# Les secrets sont montés comme variables d'environnement
db_password = os.getenv("DB_PASSWORD")
```

### 5. **Validation des Secrets**

```python
def validate_required_secrets():
    """Vérifie que tous les secrets requis sont configurés"""
    required = {
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
        "API_KEY": os.getenv("API_KEY"),
        "JWT_SECRET": os.getenv("JWT_SECRET"),
    }
    
    missing = [key for key, val in required.items() if not val]
    
    if missing:
        raise ValueError(
            f"❌ Secrets manquants: {', '.join(missing)}"
        )
    
    print("✅ Tous les secrets sont configurés")
```

### 6. **Logs Sécurisés**

```python
import logging

logger = logging.getLogger(__name__)

# ❌ VULNÉRABLE
logger.info(f"Connected to {connection_string}")  # Contient le password!

# ✅ SÉCURISÉ
logger.info(f"Connected to database at {db_host}:{db_port}")
# Ne jamais logger: passwords, tokens, API keys, secrets
```

---

## 🔧 Checklist de Sécurité

- [ ] Pas de secrets hardcodés dans le code
- [ ] Pas de secrets dans les fichiers de config commités
- [ ] Fichier .env dans .gitignore
- [ ] Variables d'environnement utilisées en dev
- [ ] Gestionnaire de secrets en production
- [ ] Logs ne contiennent pas de secrets
- [ ] Rotation régulière des secrets
- [ ] Audit de qui a accès aux secrets
- [ ] Secrets chiffrés en transit (HTTPS)
- [ ] Secrets chiffrés au repos

---

## 📚 Ressources Supplémentaires

### OWASP
- [OWASP A07:2021 - Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

### CWE
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
- [CWE-321: Use of Hard-coded Cryptographic Key](https://cwe.mitre.org/data/definitions/321.html)

### Outils pour Scanner les Secrets
```bash
# TruffleHog - Scanne les repos Git pour les secrets
pip install trufflehog
trufflehog git https://github.com/your-repo

# GitGuardian - Service cloud de détection de secrets
# https://www.gitguardian.com/

# git-secrets - Hook Git pour prévenir le commit de secrets
# https://github.com/awslabs/git-secrets

# SAST Tools - Analyse statique du code
# - SonarQube
# - Checkmarx
# - Veracode
# - Semgrep
```

---

## 🎓 Exercice d'Apprentissage

### Étape 1: Analysez le Code Vulnérable
1. Ouvrez `trap.py`
2. Identifiez TOUS les hardcoded secrets
3. Comptez combien de vulnérabilités trouvez-vous

### Étape 2: Comprenez les Risques
1. Imaginez les conséquences de chaque secret compromis
2. Tracez comment un attaquant pourrait les utiliser
3. Évaluez l'impact sur l'entreprise

### Étape 3: Étudiez la Solution
1. Ouvrez `solution.py`
2. Comparez avec le code vulnérable
3. Identifiez les 5 améliorations principales

### Étape 4: Pratiquez
1. Créez un script Python simple avec une base de données
2. Mettez d'abord des secrets en dur
3. Refactorisez pour utiliser des variables d'environnement
4. Testez avec un fichier .env

---

## 🎯 Points Clés à Retenir

1. **Les secrets ne doivent JAMAIS être dans le code**
2. **Les variables d'environnement sont le minimum**
3. **En production, utilisez un gestionnaire de secrets**
4. **Les secrets dans Git = compromis permanent**
5. **Rotation régulière = meilleure hygiène de sécurité**
6. **L'audit est crucial = qui accède aux secrets?**
7. **Les logs ne doivent pas contenir de secrets**
8. **Validez que tous les secrets requis sont configurés**

---

**Créé à des fins pédagogiques pour renforcer la sécurité informatique** 🔐
