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
- (Alain) completer funs.py + debug
- (All) 
  * Meeting with Peter Brown
  * Discuss the next steps

## 23-24/03/2025
- (Nazar) Ecritre le nouvau representation du SDP. Restructuration complet du code

## 25/03/2025

- (Thomas) begin sos problem: https://www.princeton.edu/~aaa/Public/Teaching/ORF523/ORF523_Lec15.pdf ,useful link for the sos theory
- (Yann) Migrate the branch
- (Nazar) Comancer ecrire des tests pour le nouvau code
- (Alain) Commencer d'implementer l'application Max Cut
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
- (Alain) implemented + debug de Max cut; randomized test + [example on ncpol2sdpa](https://ncpol2sdpa.readthedocs.io/en/stable/exampleshtml.html#example-1-max-cut)
- (Thomas) learn the theory of the SOS with Peter Brown


## 02/04/2025 
- (Mathis)
  * Correct apply_rule for the non commutative case
  * add tests for apply_rule

## 03/04/2025
- (Mathis)
  * Continue to implement the nc case 
    + add the function degree_of_polynomial that calculate the degree of a commutative or non commutative polynomial (sympy doesn't handle the nc cases so we had to reimplement a degree function)
- (Nazar) Cogérer des erreurs de type un peut partout. Écrire un fichier interface des types pour la bibliothèque mosek(qui n'en a pas par défaut). Recherche sur max-cut et algorithme de Goemans-Williamson

## 04/04/2025
- (Mathis)
  * Continue / finish to implement the non commutative case (not working because the SDP solver can't solve the given SDp thus the issue is perhaps on the relaxation)
  * Debug the non commutative case 
    + for the nc case, we have to double the relaxation_factor for the moement matrix (not the relaxation_factor in general) because if we don't extend the size of the moment matrix, we don't capture every monomials (eg: for the commutative case, x*y = y*x thus with monomials = (1, x, y) we generate x*y and y*x because x*y = y*x but for the non commutative case, we only capture x*y or y*x, so we have to extend the moment matrix to capture x*y and y*x by using more monomials (1, x, y, x**2, x*y, y*x, y**2) )
  * add a test for the non commutative case in test_problem.py
- (Nazar) Ecrire des interfaces de type pour les bibliothèque qu'on utilise et qui n'ont pas(cvxpy, sympy, mosek). Il sont dans la repertoire `src/typing_stubs`. Ourir un Merge Request liés aux types: !8.

## 05/04/2025
- (Mathis)
  * Review + Merge MR [!8](https://gitlab.telecom-paris.fr/proj104/2024-2025/python-poly-opt/-/merge_requests/8) that does :
    + Fix miscellaneous small type errors in the code 
    + Remove as many # type: ignore annotations as possible 
    + Write typing stubs for dependencies in src/typing_stubs. I first auto generated a template with mypy's stubgen script. Then eddied the types of functions we use in the code. The typing stubs themselves should not be typechecked
- (Alain) added functions in maxcut_example for testing efficiency of the relaxation (naive solving + bipartite graphs case)
- (Yann)
  * Read documentation about uv [link](https://docs.astral.sh/uv/concepts/projects/dependencies/#platform-specific-sources)
  * Read documentation for organize tests
  * Read documentation about pre-commit

## 08/04/2025
- (Yann)
  * Ended up to fix the branch `pydeps`
  * Try to merge

- (Thomas)
  * Begin the implementation of the SOS problem by finding the solutions of the dual problem for each constraint of the primal problem with the solver cvxpy
  * Test the code: errors remain

- (Mathis)
  * Tentative de debug de l'ajout de la partie de résolution non commutative 
    + finalement, il ne faut pas augmenter la taille de la moment matrix (*2) car sinon le problème n'est pas solvable
    + je ne comprends pas un point sur le papier de recherche pour l'implémentation de la partie non commutative, je vais voir avec Peter Brown pour mieux comprendre un point qui me pose problème