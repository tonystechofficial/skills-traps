# CONTRIBUTING.md

## 🎓 Contribution Guide for Skills Traps

Merci de votre intérêt pour contribuer à **Skills Traps**! Ce guide explique comment ajouter de nouveaux skills pièges ou améliorer les existants.

---

## 🚀 Comment Contribuer

### 1. Fork le Repository
```bash
# Visitez https://github.com/tonystechofficial/skills-traps
# Cliquez sur "Fork"
git clone https://github.com/YOUR_USERNAME/skills-traps.git
cd skills-traps
git remote add upstream https://github.com/tonystechofficial/skills-traps.git
```

### 2. Créer une Branche
```bash
git checkout -b add/new-skill-name
# ou pour bug fixes:
git checkout -b fix/bug-description
```

### 3. Ajouter un Nouveau Skill

#### Structure Requise
```
security-vulnerabilities/XX-skill-name/
├── trap.py          # ❌ Code vulnérable
├── solution.py      # ✅ Code sécurisé
└── lesson.md        # 📖 Leçon pédagogique
```

#### Fichier `trap.py`
```python
"""
🪤 PIÈGE ÉDUCATIF #XX: NOM_DU_SKILL
Vulnérabilité: Description claire
Niveau de Risque: 🔴 CRITIQUE / 🟠 MOYEN / 🟡 FAIBLE
Catégorie: Security / Performance / Logic
CWE: Numéro CWE correspondant

⚠️ ATTENTION: Code éducatif uniquement!
"""

class VulnerableClass:
    """Explication de la vulnérabilité"""
    
    def vulnerable_method(self):
        """
        ❌ VULNÉRABLE:
        - Problème 1
        - Problème 2
        - Problème 3
        """
        pass

def demonstrate_vulnerabilities():
    """Démontre les risques"""
    print("=" * 70)
    print("🪤 PIÈGE ÉDUCATIF #XX: NOM_DU_SKILL")
    print("=" * 70)
    
    # Votre démonstration
    
    print("\n" + "=" * 70)
    print("⚠️  RÉSUMÉ DES VULNÉRABILITÉS")
    print("=" * 70)
    print("""
    ❌ 1. Problème 1
    ❌ 2. Problème 2
    ❌ 3. Problème 3
    
    🔴 Risque:
       - Conséquence 1
       - Conséquence 2
    """)

if __name__ == "__main__":
    demonstrate_vulnerabilities()
```

#### Fichier `solution.py`
```python
"""
✅ SOLUTION: NOM_DU_SKILL
Vulnérabilité: Description
Niveau de Risque: 🔴 CRITIQUE → ✅ SÉCURISÉ

Bonnes pratiques appliquées:
1. ✅ Pratique 1
2. ✅ Pratique 2
3. ✅ Pratique 3
"""

class SecureClass:
    """Implémentation sécurisée"""
    
    def secure_method(self):
        """
        ✅ SÉCURISÉE:
        - Solution 1
        - Solution 2
        - Solution 3
        """
        pass

def demonstrate_secure_implementation():
    """Montre comment implémenter de manière sécurisée"""
    print("=" * 70)
    print("✅ SOLUTION SÉCURISÉE: NOM_DU_SKILL")
    print("=" * 70)
    
    print("\n[1] Approche recommandée:")
    print("-" * 70)
    print("""
    ✅ Pratique 1
    ✅ Pratique 2
    ✅ Pratique 3
    """)
    
    print("\n[2] Comparaison:")
    print("-" * 70)
    print("""
    ❌ VULNÉRABLE:
       code vulnérable
    
    ✅ SÉCURISÉ:
       code sécurisé
    """)

if __name__ == "__main__":
    demonstrate_secure_implementation()
```

#### Fichier `lesson.md`
```markdown
# Leçon #XX: Nom du Skill 🔐

## 📝 Résumé

## 🚨 Qu'est-ce qui rend le code vulnérable?

## 💥 Conséquences

## ✅ Solution

## 🔧 Checklist de Sécurité

## 📚 Ressources

## 🎓 Exercice d'Apprentissage

## 🎯 Points Clés à Retenir
```

### 4. Tester Votre Contribution

```bash
# Vérifier que les fichiers fonctionnent
python XX-skill-name/trap.py
python XX-skill-name/solution.py

# Vérifier la syntaxe
flake8 XX-skill-name/
pylint XX-skill-name/

# Vérifier le markdown
# (Lisez le fichier .md pour les erreurs)
```

### 5. Commit et Push

```bash
git add .
git commit -m "Add skill #XX: Descriptive Title

- Add trap.py with vulnerable code
- Add solution.py with secure implementation
- Add lesson.md with educational content

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

git push origin add/new-skill-name
```

### 6. Soumettre une Pull Request

1. Visitez votre fork sur GitHub
2. Cliquez sur "Create Pull Request"
3. Remplissez le template
4. Attendez la review

---

## 📋 Template PR

```markdown
## Description
Brève description du skill ajouté

## Type de Contribution
- [ ] Nouveau skill
- [ ] Bug fix
- [ ] Amélioration documentation
- [ ] Autre

## Skill Details
- **Numéro**: #XX
- **Catégorie**: Security / Performance / Logic
- **Niveau**: Débutant / Intermédiaire / Avancé
- **CWE**: CWE-XXX
- **Ressources**: Liens OWASP/CWE

## Checklist
- [ ] Code compile et s'exécute sans erreur
- [ ] `trap.py` démontre la vulnérabilité
- [ ] `solution.py` applique les bonnes pratiques
- [ ] `lesson.md` explique complètement
- [ ] Linting passe (flake8, pylint)
- [ ] Markdown formaté correctement
- [ ] Pas de secrets/credentials réels
- [ ] Disclaimer présent dans les files
```

---

## 🎯 Guidelines de Contribution

### Code Style
- Utilisez **PEP 8** pour Python
- Utilisez **black** pour formatage:
  ```bash
  black .
  ```
- Commentez le code vulnérable et explicitez les risques
- Gardez les solutions simples et pédagogiques

### Documentation
- Écrivez en **français et anglais** de préférence
- Utilisez le **markdown** correctement
- Incluez des **liens vers les ressources**
- Expliquez les **concepts** pas seulement le code

### Sécurité
- ❌ Ne jamais commit de vrais secrets
- ✅ Utilisez des valeurs d'exemple
- ⚠️ Incluez un disclaimer clairement
- 🔒 Rappelez l'usage éducatif uniquement

### Qualité
- Testez votre code avant de soumettre
- Vérifiez la grammaire et l'orthographe
- Utilisez des noms descriptifs
- Documentez les choix pédagogiques

---

## 🚫 Ce Que Nous N'Acceptons Pas

- ❌ Code non fonctionnel ou avec erreurs
- ❌ Credentials ou secrets réels
- ❌ Code sans documentation
- ❌ Vulnérabilités qui ne sont pas expliquées
- ❌ Contenu hors de scope (non-éducatif)

---

## 📞 Questions?

- Ouvrez une **Issue** pour discuter
- Vérifiez les **discussions** existantes
- Consultez le **GUIDE.md** pour plus d'infos

---

## 🎓 Code de Conduite

### Nous Attendons
✅ Respect mutuel et professionnel
✅ Focus sur l'apprentissage
✅ Contributions constructives
✅ Responsabilité pour l'usage éducatif

### Comportements Inacceptables
❌ Harcèlement ou discrimination
❌ Spam ou publicité
❌ Incitation à l'usage malveillant
❌ Discussions hors de topic

---

## 🏆 Crédits

Chaque contributeur sera crédité dans:
- README.md
- Page des contributeurs
- Commits Git

---

Merci de contribuer à l'éducation en sécurité informatique! 🎓🔐
