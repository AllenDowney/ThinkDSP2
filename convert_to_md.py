#!/usr/bin/env python3
"""
This script converts all notebooks in a directory to markdown:
- {directory}/chapXX.ipynb -> {directory}/md/chapXX.md

Usage:
    python convert_to_md.py <directory>
    python convert_to_md.py soln
    python convert_to_md.py examples

Requires: jupytext
Install with: pip install jupytext
"""

import argparse
import subprocess
import sys
from pathlib import Path


def check_jupytext():
    """Check if jupytext is installed."""
    try:
        result = subprocess.run(
            ["jupytext", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ jupytext found: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ jupytext not found. Please install it with: pip install jupytext")
        return False

def find_notebooks(directory):
    """Find all notebooks in a directory."""
    return sorted(directory.glob("*.ipynb"))



def convert_notebook(input_path, output_path):
    """Convert a notebook to markdown using jupytext."""
    try:
        result = subprocess.run(
            ["jupytext", "--to", "md", str(input_path), "-o", str(output_path)],
            capture_output=True,
            text=True,
            check=True
        )
        return True, None
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def convert_all(input_dir, md_dir):
    """Convert all notebooks in the given directory to markdown."""
    # Create output directory
    md_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all notebooks in the directory
    notebooks = find_notebooks(input_dir)
    
    print(f"Found {len(notebooks)} notebooks in {input_dir.name}/")
    
    if not notebooks:
        print("No notebooks found to convert!")
        return
    
    print("\nConverting notebooks to markdown...")
    print("=" * 60)
    
    errors = []
    converted = 0
    
    # Convert all notebooks
    for notebook in notebooks:
        notebook_in = notebook  # notebook is already a full path
        notebook_out = md_dir / notebook.with_suffix('.md').name
        success, error = convert_notebook(notebook_in, notebook_out)
        if success:
            print(f"  ✓ {input_dir.name}/{notebook.name} -> {input_dir.name}/md/{notebook_out.name}")
            converted += 1
        else:
            print(f"  ✗ {input_dir.name}/{notebook.name} failed: {error}")
            errors.append((notebook_in, error))
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Conversion complete!")
    print(f"  Converted: {converted} notebooks")
    if errors:
        print(f"  Errors: {len(errors)}")
        for path, error in errors:
            print(f"    - {path}: {error}")
    else:
        print(f"  All conversions successful ✓")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebooks to markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_to_md.py soln
  python convert_to_md.py examples
        """
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Directory containing notebooks to convert (e.g., 'soln', 'examples')"
    )
    
    args = parser.parse_args()
    
    print("Notebook to Markdown Converter")
    print("=" * 60)
    
    # Check jupytext
    if not check_jupytext():
        sys.exit(1)
    
    # Get project root and construct paths
    project_root = Path(__file__).parent
    input_dir = project_root / args.directory
    md_dir = input_dir / "md"
    
    # Verify directory exists
    if not input_dir.exists():
        print(f"✗ Directory not found: {input_dir}")
        sys.exit(1)
    
    if not input_dir.is_dir():
        print(f"✗ Not a directory: {input_dir}")
        sys.exit(1)
    
    # Convert all notebooks
    convert_all(input_dir, md_dir)


if __name__ == "__main__":
    main()
