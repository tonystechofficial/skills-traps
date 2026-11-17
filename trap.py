"""
🪤 PIÈGE ÉDUCATIF #1: HARDCODED SECRETS
Vulnérabilité: Credentials stockées en dur dans le code source
Niveau de Risque: 🔴 CRITIQUE
Catégorie: Security Vulnerability - CWE-798

⚠️ ATTENTION: Ce code ne doit JAMAIS être utilisé en production!
Ceci est un exemple intentionnel de mauvaise pratique.
"""

import requests
import json


class DatabaseConnection:
    """
    ❌ VULNÉRABLE: Les credentials sont hardcodées en dur!
    
    Problèmes:
    1. Les secrets sont visibles dans le code source
    2. Stockés dans le contrôle de version (Git)
    3. Accessibles à n'importe qui ayant accès au repo
    4. Difficiles à rotation/mise à jour
    5. Risque si le repo devient public
    """
    
    def __init__(self):
        # 🚨 HARDCODED SECRETS - NE JAMAIS FAIRE CELA!
        self.db_host = "prod-database.example.com"
        self.db_port = 5432
        self.db_username = "admin"
        self.db_password = "SuperSecretPassword123!"  # ❌ DANGER
        self.api_key = "sk-1234567890abcdefghijk"  # ❌ DANGER
        self.secret_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"  # ❌ DANGER
    
    def connect(self):
        """Établit une connexion à la base de données avec les credentials hardcodées"""
        try:
            connection_string = f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/myapp"
            print(f"[*] Tentative de connexion: {connection_string}")
            # Connexion serait établie ici
            return True
        except Exception as e:
            print(f"[-] Erreur de connexion: {e}")
            return False
    
    def call_external_api(self):
        """Appelle une API externe avec la clé API hardcodée"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "X-API-Key": self.api_key  # ❌ Double risque!
        }
        
        try:
            response = requests.get(
                "https://api.example.com/data",
                headers=headers
            )
            print(f"[*] API Response: {response.status_code}")
            return response.json()
        except Exception as e:
            print(f"[-] Erreur API: {e}")
            return None


class UserAuthenticator:
    """
    ❌ VULNÉRABLE: Stockage des credentials en dur dans la classe
    """
    
    def __init__(self):
        # 🚨 Hardcoded admin credentials
        self.admin_username = "administrator"
        self.admin_password = "AdminPass@2024"  # ❌ Visible dans le code
        self.jwt_secret = "my-super-secret-jwt-key-12345"  # ❌ Hardcodée
    
    def authenticate_user(self, username, password):
        """Vérifie les credentials d'un utilisateur"""
        if username == self.admin_username and password == self.admin_password:
            print(f"[+] Utilisateur {username} authentifié!")
            return self._generate_token(username)
        else:
            print("[-] Authentification échouée")
            return None
    
    def _generate_token(self, username):
        """Génère un JWT avec la clé secrète hardcodée"""
        import hashlib
        
        # ❌ La clé JWT secrète est en dur
        payload = f"{username}:{self.jwt_secret}"
        token = hashlib.sha256(payload.encode()).hexdigest()
        return token


class ConfigurationLeakage:
    """
    ❌ VULNÉRABLE: Exposition accidentelle de secrets dans les logs/traces
    """
    
    def __init__(self):
        self.database_url = "mysql://admin:Password123@db.example.com:3306/app"
        self.redis_password = "redis-secure-pass-789"
        self.aws_access_key = "AKIAIOSFODNN7EXAMPLE"
        self.aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    def debug_log(self):
        """❌ Enregistre les secrets complets dans les logs!"""
        print("[DEBUG] Database Configuration:")
        print(f"  URL: {self.database_url}")  # 🚨 Mot de passe en clair!
        print(f"  Redis: {self.redis_password}")  # 🚨 Mot de passe en clair!
        
        print("[DEBUG] AWS Credentials:")
        print(f"  Access Key: {self.aws_access_key}")  # 🚨 Clé en clair!
        print(f"  Secret Key: {self.aws_secret_key}")  # 🚨 Clé secrète en clair!
    
    def export_config(self):
        """❌ Exporte la config avec tous les secrets en JSON"""
        config = {
            "database": self.database_url,
            "redis": self.redis_password,
            "aws": {
                "access_key": self.aws_access_key,
                "secret_key": self.aws_secret_key
            }
        }
        
        # ❌ Enregistre en JSON avec tous les secrets!
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        print("[+] Configuration exportée dans config.json")


# ============================================================================
# DÉMONSTRATION DES VULNÉRABILITÉS
# ============================================================================

def demonstrate_vulnerabilities():
    """Montre les risques des credentials hardcodées"""
    
    print("=" * 70)
    print("🪤 PIÈGE ÉDUCATIF: HARDCODED SECRETS")
    print("=" * 70)
    
    # 1. Database Connection
    print("\n[1] Attempting Database Connection...")
    db = DatabaseConnection()
    db.connect()
    print(f"    Password exposée: {db.db_password}")
    print(f"    API Key exposée: {db.api_key}")
    
    # 2. User Authentication
    print("\n[2] User Authentication...")
    auth = UserAuthenticator()
    token = auth.authenticate_user("administrator", "AdminPass@2024")
    print(f"    JWT Secret exposée: {auth.jwt_secret}")
    
    # 3. Configuration Leakage
    print("\n[3] Configuration Leakage...")
    config = ConfigurationLeakage()
    config.debug_log()
    config.export_config()
    
    print("\n" + "=" * 70)
    print("⚠️  RÉSUMÉ DES VULNÉRABILITÉS DÉMONTRÉES:")
    print("=" * 70)
    print("""
    ❌ 1. Credentials en dur dans le code source
    ❌ 2. Secrets visibles dans le contrôle de version Git
    ❌ 3. Clés API exposées dans les requêtes
    ❌ 4. Secrets dans les fichiers de configuration JSON
    ❌ 5. Secrets affichés dans les logs de debug
    ❌ 6. JWT secrets hardcodées
    ❌ 7. Pas de rotation de credentials possible
    
    🔴 Risque: N'importe qui avec accès au code peut:
       - Se connecter à la base de données
       - Accéder aux APIs externes
       - Usurper l'identité d'administrateurs
       - Accéder aux services AWS
       - Compromettre toute l'infrastructure
    """)


if __name__ == "__main__":
    demonstrate_vulnerabilities()
