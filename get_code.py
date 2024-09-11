import os
import argparse
import sys
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern

def is_code_file(filename):
    # Add or remove extensions based on your needs
    code_extensions = ['.py', '.js', '.java', '.cpp', '.c', '.h', '.css', '.html', '.php', '.rb', '.go', '.ts', '.tsx']
    return any(filename.endswith(ext) for ext in code_extensions)

def get_gitignore_spec(root_dir):
    gitignore_path = os.path.join(root_dir, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            return PathSpec.from_lines(GitWildMatchPattern, gitignore_file)
    return None

def process_codebase(root_dir, output_file, exclude_dirs):
    script_name = os.path.basename(__file__)
    gitignore_spec = get_gitignore_spec(root_dir)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(root_dir):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            # Remove directories specified in .gitignore
            if gitignore_spec:
                dirs[:] = [d for d in dirs if not gitignore_spec.match_file(os.path.join(root, d))]
            
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, root_dir)
                
                # Skip files specified in .gitignore
                if gitignore_spec and gitignore_spec.match_file(relative_path):
                    continue
                
                if is_code_file(file) and file != script_name:
                    out_file.write(f"```{relative_path}\n")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as code_file:
                            lines = code_file.readlines()
                            for line_number, line in enumerate(lines, 1):
                                out_file.write(f"{line_number:4d} | {line}")
                    except UnicodeDecodeError:
                        out_file.write(f"Unable to read file: {relative_path}\n")
                    
                    out_file.write("```\n\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown document from a codebase.")
    parser.add_argument("root_dir", help="Root directory of the codebase")
    parser.add_argument("output_file", help="Output Markdown file")
    parser.add_argument("--exclude", nargs='+', default=[], help="Additional directories to exclude")
    
    args = parser.parse_args()
    
    process_codebase(args.root_dir, args.output_file, args.exclude)
    print(f"Markdown document generated: {args.output_file}")

if __name__ == "__main__":
    main()