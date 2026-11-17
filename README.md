# Skills Traps 🪤

Une collection de **skills éducatifs pièges** pour apprendre les vulnérabilités de sécurité, les anti-patterns de performance et les erreurs logiques courantes en programmation.

## Objectif

Ce dépôt est conçu à des **fins pédagogiques uniquement**. Chaque skill contient intentionnellement des vulnérabilités ou des mauvaises pratiques pour :

- ✅ Identifier les patterns dangereux
- ✅ Comprendre les conséquences de code insécurisé
- ✅ Apprendre comment corriger les vulnérabilités
- ✅ Renforcer les bonnes pratiques de développement

⚠️ **ATTENTION** : Ne jamais utiliser ce code en production. Ces skills sont uniquement pour l'apprentissage.

---

## 📂 Structure du Dépôt

```
skills-traps/
├── README.md
├── security-vulnerabilities/
│   ├── 01-hardcoded-secrets/
│   │   ├── trap.py
│   │   ├── solution.py
│   │   └── lesson.md
│   ├── 02-sql-injection/
│   │   ├── trap.py
│   │   ├── solution.py
│   │   └── lesson.md
│   └── 03-command-injection/
│       ├── trap.py
│       ├── solution.py
│       └── lesson.md
├── performance-antipatterns/
├── logic-errors/
└── docs/
    └── GUIDE.md
```

---

## 🪤 Skills Disponibles

### Sécurité

#### 1️⃣ Hardcoded Secrets (Secrets en dur)
**Niveau**: Débutant  
**Vulnérabilité**: Credentials stockées en clair dans le code  
**Leçon**: Comment sécuriser les secrets avec des variables d'environnement

#### 2️⃣ SQL Injection
**Niveau**: Intermédiaire  
**Vulnérabilité**: Entrée utilisateur directement concaténée en SQL  
**Leçon**: Utiliser les parameterized queries et input validation

#### 3️⃣ Command Injection
**Niveau**: Intermédiaire  
**Vulnérabilité**: Exécution de commandes système sans sanitization  
**Leçon**: Valider et échapper les entrées utilisateur

---

## 🎓 Comment Utiliser

### Étape 1: Lire le Piège
```bash
cd security-vulnerabilities/01-hardcoded-secrets
cat trap.py
```

### Étape 2: Identifier la Vulnérabilité
Analysez le code et trouvez le problème de sécurité.

### Étape 3: Consulter la Leçon
```bash
cat lesson.md
```

### Étape 4: Voir la Solution
```bash
cat solution.py
```

### Étape 5: Tester le Code
```bash
python trap.py          # Montrera la vulnérabilité
python solution.py      # Affichera la version sécurisée
```

---

## 📚 Guide Complet

Consultez [GUIDE.md](./docs/GUIDE.md) pour :
- Comment configurer l'environnement
- Explication détaillée de chaque vulnérabilité
- Bonnes pratiques pour chaque catégorie
- Ressources externes pour approfondir

---

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/tonystechofficial/skills-traps.git
cd skills-traps

# Installer les dépendances (optionnel)
pip install -r requirements.txt
```

---

## 🔒 Responsabilité

Ce dépôt est fourni à des fins éducatives. Les utilisateurs sont responsables de :

- ✅ N'utiliser ce code qu'à titre pédagogique
- ✅ Ne jamais adapter ces patterns à un code production
- ✅ Comprendre les implications de sécurité
- ✅ Respecter les législations et politiques d'entreprise

---

## 📖 Ressources Recommandées

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Most Dangerous Weaknesses](https://cwe.mitre.org/top25/)
- [Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [SANS Top 25 Software Errors](https://www.sans.org/top25-software-errors/)

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour ajouter un nouveau skill piège :

1. Créez un dossier avec un nom descriptif
2. Incluez `trap.py`, `solution.py` et `lesson.md`
3. Testez votre code
4. Soumettez une PR

---

## 📄 Licence

MIT License - Voir [LICENSE](./LICENSE) pour plus de détails.

---

## ⚡ Disclaimer

**Ce code ne doit JAMAIS être utilisé en production.**  
Ceci est un projet éducatif. L'auteur n'est pas responsable de l'utilisation abusive ou de dommages causés par ce code.

---

**Créé avec 🎓 pour l'apprentissage en sécurité informatique**
