#!/usr/bin/env python3
"""
Utility script to convert coverage.xml file to HTML report for better visualization.
"""

import argparse
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime


def generate_html_report(xml_file: str, output_dir: str) -> bool:
    """Generate HTML coverage report from XML file."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Extract coverage summary data
        timestamp = int(root.get("timestamp", "0")) / 1000  # Convert to seconds
        date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        lines_valid = int(root.get("lines-valid", "0"))
        lines_covered = int(root.get("lines-covered", "0"))
        line_rate = float(root.get("line-rate", "0"))
        coverage_percent = f"{line_rate * 100:.2f}%"

        # Generate index file with summary
        with open(os.path.join(output_dir, "index.html"), "w") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Coverage Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2 {{ color: #333; }}
        .summary {{ background-color: #f8f8f8; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .good {{ color: green; }}
        .bad {{ color: red; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #f5f5f5; }}
        .package-name {{ font-weight: bold; }}
        .progress-bar-container {{ width: 100px; background-color: #e0e0e0; height: 15px; border-radius: 10px; }}
        .progress-bar {{ background-color: #4CAF50; height: 15px; border-radius: 10px; }}
        .module-link {{ text-decoration: none; color: #0066cc; }}
        .module-link:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Coverage Report</h1>

    <div class="summary">
        <p>Generated on: {date_str}</p>
        <p>Lines covered: {lines_covered} / {lines_valid}</p>
        <p>Coverage: <span class="{"good" if line_rate >= 0.8 else "bad"}">{coverage_percent}</span></p>
    </div>

    <h2>Packages</h2>
    <table>
        <tr>
            <th>Package</th>
            <th>Coverage</th>
            <th>Visualization</th>
        </tr>
""")

            # Add package data
            for package in root.findall("./packages/package"):
                pkg_name = package.get("name", "unknown")
                pkg_rate = float(package.get("line-rate", "0"))
                pkg_percent = f"{pkg_rate * 100:.2f}%"
                bar_width = int(pkg_rate * 100)

                pkg_file = f"{pkg_name.replace('.', '_')}.html"

                f.write(f"""
        <tr>
            <td class="package-name"><a href="{pkg_file}" class="module-link">{pkg_name}</a></td>
            <td>{pkg_percent}</td>
            <td>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {bar_width}%"></div>
                </div>
            </td>
        </tr>""")

                # Create package detail page
                generate_package_page(
                    package, os.path.join(output_dir, pkg_file), pkg_name
                )

            f.write("""
    </table>
</body>
</html>""")

        return True

    except Exception as e:
        print(f"Error generating HTML report: {e}")
        return False


def generate_package_page(package: ET.Element, output_file: str, pkg_name: str) -> None:
    """Generate HTML page for a specific package."""
    with open(output_file, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Coverage Report - {pkg_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1, h2 {{ color: #333; }}
        .summary {{ background-color: #f8f8f8; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .good {{ color: green; }}
        .bad {{ color: red; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
        th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        tr:hover {{ background-color: #f5f5f5; }}
        .progress-bar-container {{ width: 100px; background-color: #e0e0e0; height: 15px; border-radius: 10px; }}
        .progress-bar {{ background-color: #4CAF50; height: 15px; border-radius: 10px; }}
        .back-link {{ margin-bottom: 20px; display: block; }}
        .module {{ margin-bottom: 30px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }}
        .module-title {{ margin-top: 0; }}
        .line {{ font-family: monospace; white-space: pre; }}
        .hit {{ background-color: #ceffce; }}
        .miss {{ background-color: #ffcece; }}
    </style>
</head>
<body>
    <a href="index.html" class="back-link">← Back to Summary</a>
    <h1>Package: {pkg_name}</h1>

    <div class="summary">
        <p>Coverage: <span class="{"good" if float(package.get("line-rate", "0")) >= 0.8 else "bad"}">{float(package.get("line-rate", "0")) * 100:.2f}%</span></p>
    </div>

    <h2>Modules</h2>
    <table>
        <tr>
            <th>Module</th>
            <th>Coverage</th>
            <th>Visualization</th>
        </tr>
""")

        # Add class (module) data
        for cls in package.findall("./classes/class"):
            cls_name = cls.get("name", "unknown")
            cls_rate = float(cls.get("line-rate", "0"))
            cls_percent = f"{cls_rate * 100:.2f}%"
            bar_width = int(cls_rate * 100)

            f.write(f"""
        <tr>
            <td>{cls_name}</td>
            <td>{cls_percent}</td>
            <td>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {bar_width}%"></div>
                </div>
            </td>
        </tr>""")

        f.write("""
    </table>

    <h2>Module Details</h2>
""")

        # Add detailed line coverage for each module
        for cls in package.findall("./classes/class"):
            cls_name = cls.get("name", "unknown")
            filename = cls.get("filename", "")

            f.write(f"""
    <div class="module">
        <h3 class="module-title">{cls_name}</h3>
        <p>Filename: {filename}</p>
        <p>Coverage: {float(cls.get("line-rate", "0")) * 100:.2f}%</p>

        <h4>Line Coverage</h4>
        <table>
            <tr>
                <th>Line #</th>
                <th>Hits</th>
                <th>Status</th>
            </tr>
""")

            # Add line coverage details
            for line in cls.findall("./lines/line"):
                line_num = line.get("number", "?")
                hits = line.get("hits", "0")
                status = "hit" if int(hits) > 0 else "miss"
                status_text = "✓" if int(hits) > 0 else "✗"

                f.write(f"""
            <tr class="{status}">
                <td>{line_num}</td>
                <td>{hits}</td>
                <td>{status_text}</td>
            </tr>""")

            f.write("""
        </table>
    </div>
""")

        f.write("""
</body>
</html>""")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert XML coverage report to HTML")
    parser.add_argument(
        "--xml-file", default="coverage.xml", help="Path to the coverage XML file"
    )
    parser.add_argument(
        "--output-dir",
        default="docs/htmlcov",
        help="Directory to output HTML coverage report",
    )
    args = parser.parse_args()

    if not os.path.exists(args.xml_file):
        print(f"Error: Coverage file '{args.xml_file}' not found")
        return 1

    print(f"Generating HTML report from {args.xml_file}...")
    if generate_html_report(args.xml_file, args.output_dir):
        print(f"\nHTML coverage report generated at: {args.output_dir}/index.html")
        print(
            f"You can open it with: firefox {os.path.abspath(args.output_dir)}/index.html"
        )
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
