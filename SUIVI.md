# Suivi

## 14/02/2025

- (Nazar) Setup du git 
- (Nazar) Organization des sources
- (Tous) Prends en main de l'article revue (Tavakoli Pozas-Kerstjens Brown Ara\'ujo)
- (Tous) faire les exercies envoyé par l'encadrant.
- (Tous) Première prise en main avec [picos](https://picos-api.gitlab.io/picos/)
- (Nazar) essayer de faire marcher PICO avec un probleme k=2 (echeque)

## 18/02/2025

- (Mathis) implementation de la résolution du SDP niveau 2 de l'exercice 2 avec cvxpy (resultat bizarre, solution non bornée)
- (Nazar) Reproduire le resultat de Mathis que l'exo 3 n'est pas borné.
- (Yann) Résolution de l'exercice 2 à la main
- (Tous) Rendez-vous avec l'encadrant à 10h30 pour discuter de notre avancement
- (Thomas et Mathis) Résolution exercice 3 donné par l'encadrant

## 20/02/2025

- (Tous) Rendez-vous avec l'encadrant pour discuter de notre organisation et du plan
- (Tous) Premiers templates pour la structure du code

## 21/02/2025

- (Mathis) 
  * implémentation des fonctions rule_of_constraint et rule_of_constraints
  * ajout de fonctions de test avec pytest

## 04/03/2025

- (Tous) RDV avec Peter Brown 
- (Mathis) 
  * ajout de la fonction needed_monomials + tests
- (Nazar) fonction pour generer tous les monomes   
- (Yann) ajout du gestionnaire uv

## 06/03/2025
 - (Nazar) Ajouter les appels de fonction dans problem.py. ajouter fonction dictionaire dans monmial.py
 - (Mathis) ajout de la fonction create_moment_matrix + tests

## 11/03/2025
- (Nazar et Thomas) première version du solveur utilisant cvxpy
- (Mathis) 
  * correction de logique dans la création des matrices de moments (changement de variable)
  * ajout de test pour le problème finale 
  * aide pour le solveur
- (Yann) 
  * Reformat src
  * Reformat test
  * Add mypy and ruff integration details to README
  * update pyproject.toml for mypy dependency
  * add new test for typing functionality

## 12/03/2024
- (Mathis) 
  * ajout de test pour la partie solver.py
  * debug de solver.py

## 14/03/2025

- (Mathis)
  * debug de problem.py
  * ajout de la substitution dans le code général (ne marche pas mais ne créer pas d'autre bug (on peut ne pas activer les substitutions))

## 15/03/2025

- (Mathis) debug
- (Yann) 
  * Clean and refactor the code
  * Add typing annotations.

## 18/03/2025 

- (Mathis) debug + test
- (Yann)
  * Add sphinx to the project
  * Clean, refactor and add type annotations to the code
- (Nazar) Commencer à faire un nouvau type de données pour mieux representer des SDPs sur la branche better-sdp-representation.
- (All) 
  * Meeting with Peter Brown
  * Discuss the next steps

## 23-24/03/2025
- (Nazar) Ecritre le nouvau representation du SDP. Restructuration complet du code

## 25/03/2025

- (Thomas) begin sos problem: https://www.princeton.edu/~aaa/Public/Teaching/ORF523/ORF523_Lec15.pdf ,useful link for the sos theory
- (Yann) Migrate the branch
- (Nazar) Comancer ecrire des tests pour le nouvau code
- (Allain) Comancer d'implementaer une application: Max Cut
- (Mathis) Lecture et compréhension de la nouvelle implémentation du solveur

## 27/03/2025

- (Nazar) Refacturation du code. Merge un changement important

## 30/03/2025
- (Nazar) Recherche sur util pre-commit(pre-commit.com)
- (Nazar) Commencer de implementer du "property based testing" avec bibliothèque hypothesis(hypothesis.works) 
- (Mathis) Apprentissage de mosek pour sa futur implémentation + apprentissage du nouveau code (surtout sur la partie solver SDP donc output de ce qui précède)

## 31/03/2025
- (Mathis) Add the mosek solver to solve the SDP, include tests with Mosek and a functionnality to choose which solver use. [A more detailed explanation of the MR can be found here](https://gitlab.telecom-paris.fr/proj104/2024-2025/python-poly-opt/-/merge_requests/4)
- (Nazar) Review the Mathis's merge_requests and sugest changes.
- (Yann)
  * Add the Mosek license for pipeline

## 01/04/2025
- (Yann)
  * Add documentation with sphinx
- (Mathis)
  * Start to implement the non commutative part of the problem
    + create a function generate_monomials_non_commutative that returns a list of all monomials of a degree less than the relaxation parameter that are non commutative
    + implement a new function apply_rule_non_commutative that is a generalisation of the function apply_rule for non commutative monomials
- (Nazar) Merge the [MR](https://gitlab.telecom-paris.fr/proj104/2024-2025/python-poly-opt/-/merge_requests/4). Add a merge request for the pre-commit tool: [!2](https://gitlab.telecom-paris.fr/proj104/2024-2025/python-poly-opt/-/merge_requests/6)

