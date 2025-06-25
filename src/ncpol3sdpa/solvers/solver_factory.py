from typing import Any, Dict, Optional, Type

from .solver import Solver
from .cvxpy_solver import CvxpySolver
from .mosek_solver import MosekSolver

class SolverFactory:
    """
    Factory class for creating instances of the appropriate solver based on configuration.
    """
    
    # Dictionary mapping solver names to solver classes
    _solver_map: Dict[str, Type[Solver]] = {
        "cvxpy": CvxpySolver,
        "mosek": MosekSolver
    }
    
    @classmethod
    def create_solver(cls, solver_name: str, config: Optional[Dict[str, Any]] = None) -> Solver:
        """
        Create an instance of the specified solver.
        
        Args:
            solver_name (str): Name of the solver to create
            config (dict, optional): Configuration parameters for the solver.
            
        Returns:
            Solver: An instance of the specified solver.

        Raises:
            ValueError: If the specified solver is not found in the factory.

        Example:
            >>> config = {"param1": "value1", "param2": "value2"}
            >>> solver = SolverFactory.create_solver("cvxpy", config)
        """
        solver_class = cls._solver_map.get(solver_name.lower())
        
        if solver_class is None:
            raise ValueError(f"Unknown solver: {solver_name}. Available solvers: {list(cls._solver_map.keys())}")
        
        kwargs = config or {}
        # Create an instance of the solver with config if provided, otherwise no args
        solver = solver_class(**kwargs)

        # Check if the solver is available (all dependencies installed)
        if solver.is_available():
            return solver
        raise ValueError(f"Solver {solver_name} is not available. Please install the required dependencies.")
    
    @classmethod
    def get_available_solvers(cls) -> Dict[str, Type[Solver]]:
        """
        Get a dictionary of all available solvers.
        
        Returns:
            Dict[str, Type[Solver]]: Dictionary mapping solver names to solver classes for solvers that are available.
        """
        available_solvers = {}
        
        for name, solver_class in cls._solver_map.items():
            # Create a temporary instance to check availability
            solver = solver_class()
            if solver.is_available():
                available_solvers[name] = solver_class
        
        return available_solvers

    @classmethod
    def get_solver(cls, solver_name: str) -> Type[Solver]:
        """
        Get the solver class for the specified solver name.

        Args:
            solver_name (str): Name of the solver to retrieve.

        Returns:
            Type[Solver]: The solver class corresponding to the specified name.

        Raises:
            ValueError: If the specified solver is not found.
        """
        if solver_name.lower() in cls._solver_map:
            return cls._solver_map[solver_name.lower()]
        else:
            raise ValueError(f"Solver {solver_name} not found. Available solvers: {list(cls._solver_map.keys())}")