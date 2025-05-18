# Presentation Audit

## Présentation du Problème

Notre projet vise à développer une nouvelle bibliothèque Python pour l'optimisation polynomiale, nommée ncpol3sdpa. Cette bibliothèque sera le successeur de ncpol2sdpa, un outil utilisé pour calculer des approximations aux problèmes d'optimisation polynomiale.

### Contexte Mathématique

L'optimisation polynomiale cherche à résoudre des problèmes de la forme :

$$\begin{align*}
\max_{x_1, \ldots, x_n} &\quad f(x_1, \ldots, x_n) \\
\text{s.t.} &\quad g_i(x_1, \ldots, x_n) \leq 0 \quad \forall i
\end{align*}$$

où $f,g_i \in \mathbb K [x_1,\ldots,x_n]$. Ces problèmes sont NP-difficiles mais peuvent être approximés par des techniques d'optimisation convexe basées sur les matrices de moments et les polynômes sommes de carrés.

## Enjeux et Objectifs

Notre bibliothèque vise à :

1. **Moderniser l'approche** : Créer une version plus flexible et efficace que ncpol2sdpa
2. **Améliorer les performances** : Optimiser les calculs pour des problèmes complexes
3. **Utiliser plusieurs solvers** : Intégrer différents solveurs pour élargir les possibilités de résolution

## Notre Équipe

Alain: maxcut  
Mathis: polynômes complexes et non commutatifs  
Nazar: tests et intégration continue  
Thomas: SOS decomposition  
Yann: organisation technique  

## Organisation du Travail

### Répartition des Tâches

Nous avons organisé notre travail en modules distincts :
- Implémentation du noyau mathématique
- Développement des interfaces utilisateur
- Tests et validation
- Documentation et exemples d'utilisation

### Méthodologie

- **Développement par branche** : Chaque membre travaille sur une branche dédiée. Les branches sont fusionnées toutes les deux semaines.
- **Revues de code** systématiques avant intégration
- **Tests unitaires** et intégration continue
- **Réunions bimensuel** avec notre superviseur (Peter Brown)

### Planning

#### Objectifs fin P3:

Cas d'optimisation des polynomes commutatifs et réel
- [x] Partie "Algèbre", manipulation symbolique des polynômes
- [x] Construction de la matrice des moments de Lassere
- [x] Communication avec des solveurs de SDP

#### Objectifs fin P4:

- [ ] Documentation, tutoriel et exemples
- [x] Jeux des tests (CI/CD)
- [x] Cas de polynomes complexe
- [ ] Cas de polynomes non Comutative
- [ ] Optimisations pour aller plus vite

<!-- ## Défis Techniques

- Conception d'une architecture flexible pour intégrer de futures avancées théoriques
- Optimisation des performances pour les problèmes à grande échelle
- Gestion des cas particuliers (variables non commutatives)
- Compatibilité avec l'écosystème Python scientifique actuel -->

## Applications et Impact

Notre bibliothèque pourra être utilisée en informatique quantique et en théorie de l'information quantique, principalement pour la résolution de problèmes d'optimisation dans ces domaines. 
La bibliothèque `ncpol2sdpa` est actuellement utilisée par des chercheurs dans ces domaines.

