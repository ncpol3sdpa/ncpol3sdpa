#!/usr/bin/env python3
"""
Script to automatically generate RST documentation files for the ncpol3sdpa package.
This script creates documentation files for the core modules of the project.
"""

import os

def generate_RST_files() -> None:
    # Get the project root directory and docs source directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = script_dir
    
    print(f"Output directory: {output_dir}")
    
    # Define core modules to document - using direct module paths
    core_modules = [
        ('ncpol3sdpa.problem', 'Problem'),

        ('ncpol3sdpa.resolution.algebra', 'Algebra'),
        ('ncpol3sdpa.resolution.constraints', 'Constraints'),
        ('ncpol3sdpa.resolution.create_algebra', 'CreateAlgebra'),
        ('ncpol3sdpa.resolution.monomial', 'Monomial'),
        ('ncpol3sdpa.resolution.rules', 'Rules'),

        ('ncpol3sdpa.sdp_repr.problem_SDP', 'ProblemSDP'),
        ('ncpol3sdpa.sdp_repr.moment_matrix_SDP', 'MomentMatrixSDP'),


        ('ncpol3sdpa.solvers.solver', 'Solver'),
        ('ncpol3sdpa.solvers.solver_registry', 'SolverRegistry'),
    ]
    
    # Generate RST files for core modules
    generated_modules = []
    for module_name, file_name in core_modules:
        print(f"Generating documentation for {module_name}")
        file_path = os.path.join(output_dir, f"generated/{file_name}.rst")
        
        display_name = file_name.replace('_', ' ').title()
        content = f"""{display_name}
{'=' * len(display_name)}

.. automodule:: {module_name}
   :members:
   :undoc-members:
   :show-inheritance:
"""
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        generated_modules.append(file_name)
    
    print(f"Generated documentation for {len(generated_modules)} modules")
    return

if __name__ == "__main__":
    generate_RST_files()
