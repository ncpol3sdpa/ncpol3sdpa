#!/usr/bin/env python3
"""
Script to automatically generate RST documentation files for the ncpol3sdpa package.
This script creates documentation files for the core modules of the project.
"""

import os


def generate_RST_files() -> None:
    print("Generating RST documentation files...")

    # Get the project root directory and docs source directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = script_dir

    print(f"Output directory: {output_dir}")

    # Define core modules to document - using direct module paths
    core_modules = [
        # ("ncpol3sdpa.resolution.algebra", "Algebra"),
        ("ncpol3sdpa.resolution.constraints", "Constraints"),
        # ("ncpol3sdpa.resolution.create_algebra", "CreateAlgebra"),
        # ("ncpol3sdpa.resolution.monomial", "Monomial"),
        # ("ncpol3sdpa.resolution.rules", "Rules"),
        # ("ncpol3sdpa.resolution.utils", "Utils"),
        # ("ncpol3sdpa.sdp_repr.eq_constraint", "EqConstraint"),
        # ("ncpol3sdpa.sdp_repr.moment_matrix_SDP", "MomentMatrixSDP"),
        # ("ncpol3sdpa.sdp_repr.problem_SDP", "ProblemSDP"),
        ("ncpol3sdpa.solvers.solver_factory", "SolverFactory"),
        ("ncpol3sdpa.solvers.solver", "Solver"),
        # ("ncpol3sdpa.algebra_to_SDP", "AlgebraToSDP"),
        # ("ncpol3sdpa.funs", "Funs"),
        ("ncpol3sdpa.problem", "Problem"),
        ("ncpol3sdpa.sos", "SOS"),
    ]

    # Clean up existing API directory
    api_dir = os.path.join(output_dir, "api")
    if os.path.exists(api_dir):
        print(f"Removing existing API directory: {api_dir}")
        for root, dirs, files in os.walk(api_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))

    # Generate RST files for core modules
    generated_modules = []
    for module_name, file_name in core_modules:
        print(f"Generating documentation for {module_name}")
        file_path = os.path.join(output_dir, f"api/{file_name}.rst")

        display_name = file_name.replace("_", " ").title()
        content = f"""{display_name}
{"=" * len(display_name)}

.. automodule:: {module_name}
   :members:
   :undoc-members:
   :show-inheritance:
"""

        with open(file_path, "w") as f:
            f.write(content)

        generated_modules.append(file_name)

    print(f"Generated documentation for {len(generated_modules)} modules")
    return


if __name__ == "__main__":
    generate_RST_files()
