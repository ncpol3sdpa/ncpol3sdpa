#!/usr/bin/env python3
"""
Script to automatically generate RST documentation files for the ncpol3sdpa package.
This script creates documentation files for the core modules of the project.
"""

import os
import sys

def main() -> int:
    # Get the project root directory and docs source directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = script_dir
    
    print(f"Output directory: {output_dir}")
    
    # Define core modules to document - using direct module paths
    core_modules = [
        ('ncpol3sdpa.problem', 'problem'),
        ('ncpol3sdpa.resolution.constraints', 'constraints'),
        ('ncpol3sdpa.resolution.rules', 'rules'),
        ('ncpol3sdpa.resolution.monomial', 'monomial'),
        ('ncpol3sdpa.resolution.algebra', 'momentmatrix'),
        ('ncpol3sdpa.solvers.solver_registry', 'solver'),
        ('ncpol3sdpa.algebra_to_SDP', 'funs'),
    ]
    
    # Generate RST files for core modules
    generated_modules = []
    for module_name, file_name in core_modules:
        print(f"Generating documentation for {module_name}")
        file_path = os.path.join(output_dir, f"{file_name}.rst")
        
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
    return 0

if __name__ == "__main__":
    sys.exit(main())
