# 🚀 Démarrage Rapide - Skills Traps

## En 5 Minutes ⏱️

### 1. Cloner le Repository
```bash
git clone https://github.com/tonystechofficial/skills-traps.git
cd skills-traps
```

### 2. Explorer le Skill Piège
```bash
# Voir le code VULNÉRABLE
cat security-vulnerabilities/01-hardcoded-secrets/trap.py

# Lire la LEÇON pédagogique
cat security-vulnerabilities/01-hardcoded-secrets/lesson.md

# Voir la SOLUTION sécurisée
cat security-vulnerabilities/01-hardcoded-secrets/solution.py
```

### 3. Exécuter le Code
```bash
# Montrer les risques des secrets hardcodés
python security-vulnerabilities/01-hardcoded-secrets/trap.py

# Montrer la solution sécurisée
python security-vulnerabilities/01-hardcoded-secrets/solution.py
```

### 4. Approfondir
Lisez `GUIDE.md` pour plus de détails et de ressources.

---

## 🎓 Structure d'Apprentissage Proposée

```
1️⃣  Identifier
    └─ Lire trap.py
       Trouvez TOUS les hardcoded secrets
       Comptez les vulnérabilités

2️⃣  Comprendre
    └─ Lire lesson.md
       Comprenez WHY c'est vulnérable
       Explorez les conséquences

3️⃣  Apprendre
    └─ Lire solution.py
       Comparez avec trap.py
       Identifiez les changements clés

4️⃣  Pratiquer
    └─ Créer votre propre code
       Appliquez les bonnes pratiques
       Testez votre implémentation
```

---

## 🔒 Points Clés du Skill #1

### ❌ VULNÉRABLE
```python
password = "SuperSecretPassword123!"  # Dans le code source
api_key = "sk-1234567890abcdefghijk"  # Visible dans Git
db_url = f"psql://user:{pwd}@host"    # Dans les logs!
```

### ✅ SÉCURISÉ
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Charger depuis .env

password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")
# Les secrets viennent de l'environnement, pas du code!
```

---

## 📚 Ressources Rapides

| Ressource | Lien |
|-----------|------|
| OWASP Top 10 | https://owasp.org/Top10/ |
| CWE-798 | https://cwe.mitre.org/data/definitions/798.html |
| Python Secrets | https://docs.python.org/3/library/secrets.html |
| .gitignore Guide | https://github.com/github/gitignore |

---

## ⚡ Commandes Utiles

```bash
# Installer les dépendances
pip install -r requirements.txt

# Scanner pour les secrets dans Git
pip install truffleHog
truffleHog git https://github.com/tonystechofficial/skills-traps

# Analyser le code pour les vulnérabilités
pip install bandit
bandit -r .

# Vérifier la qualité du code
pip install flake8
flake8 .
```

---

## 🎯 Objectif

Après 1 heure d'étude, vous devriez pouvoir:
✅ Identifier les hardcoded secrets dans le code
✅ Comprendre les risques de sécurité
✅ Implémenter les bonnes pratiques
✅ Utiliser les variables d'environnement
✅ Protéger votre projet

---

## 🆘 Problèmes Courants

### ImportError: No module named 'dotenv'
```bash
pip install python-dotenv
```

### "Cannot find module 'requests'"
```bash
pip install -r requirements.txt
```

### Git permissions denied
```bash
# Assurez-vous d'avoir configuré vos clés SSH
ssh -T git@github.com
```

---

## 📞 Besoin d'Aide?

1. **Consultez** GUIDE.md pour plus de détails
2. **Lisez** lesson.md pour les explications
3. **Ouvrez une Issue** sur GitHub
4. **Vérifiez** les discussions existantes

---

**Prêt à améliorer votre sécurité informatique?** 🔐

Commencez par le Skill #1: Hardcoded Secrets
