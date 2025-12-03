from datetime import timezone
import git
import pathlib
import sqlite_utils
import json


root = pathlib.Path(__file__).parent.resolve()


def created_changed_times(repo_path, ref="main"):
    created_changed_times = {}
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref)))
    for commit in commits:
        dt = commit.committed_datetime
        affected_files = list(commit.stats.files.keys())
        for filepath in affected_files:
            if filepath not in created_changed_times:
                created_changed_times[filepath] = {
                    "created": dt.isoformat(),
                    "created_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            created_changed_times[filepath].update(
                {
                    "updated": dt.isoformat(),
                    "updated_utc": dt.astimezone(timezone.utc).isoformat(),
                }
            )
            
    return created_changed_times


def extract_notebook_content(filepath):
    """Extract title and body from a Jupyter notebook."""
    with open(filepath, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    title = None
    body_parts = []
    
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            # Convert source to string (it can be a list or string)
            if isinstance(source, list):
                content = ''.join(source)
            else:
                content = source
            
            # Extract title from first heading if not yet found
            if title is None:
                lines = content.split('\n')
                for line in lines:
                    if line.strip().startswith('#'):
                        title = line.lstrip('#').strip()
                        break
            
            body_parts.append(content)
    
    # If no title found, use filename
    if title is None:
        title = filepath.stem.replace('_', ' ').replace('-', ' ').title()
    
    body = '\n\n'.join(body_parts).strip()
    return title, body


def build_database(repo_path):
    all_times = created_changed_times(repo_path)
    db = sqlite_utils.Database(repo_path / "til.db")
    table = db.table("til", pk="path")
    
    # Process markdown files
    for filepath in root.glob("*/*.md"):
        fp = filepath.open()
        title = fp.readline().lstrip("#").strip()
        body = fp.read().strip()
        path = str(filepath.relative_to(root))
        url = "https://github.com/marcelcastrobr/til/blob/main/{}".format(path)
        record = {
            "path": path.replace("/", "_"),
            "topic": path.split("/")[0],
            "title": title,
            "url": url,
            "body": body,
        }
        record.update(all_times[path])
        table.insert(record, replace=True)
    
    # Process Jupyter notebook files in subdirectories
    for filepath in root.glob("*/*.ipynb"):
        title, body = extract_notebook_content(filepath)
        path = str(filepath.relative_to(root))
        url = "https://github.com/marcelcastrobr/til/blob/main/{}".format(path)
        record = {
            "path": path.replace("/", "_"),
            "topic": path.split("/")[0],
            "title": title,
            "url": url,
            "body": body,
        }
        record.update(all_times[path])
        table.insert(record, replace=True)
    
    # Process Jupyter notebook files in root directory
    for filepath in root.glob("*.ipynb"):
        title, body = extract_notebook_content(filepath)
        path = str(filepath.relative_to(root))
        url = "https://github.com/marcelcastrobr/til/blob/main/{}".format(path)
        record = {
            "path": path.replace("/", "_"),
            "topic": "notebooks",  # Default topic for root-level notebooks
            "title": title,
            "url": url,
            "body": body,
        }
        record.update(all_times[path])
        table.insert(record, replace=True)
    
    if "til_fts" not in db.table_names():
        table.enable_fts(["title", "body"])


if __name__ == "__main__":
    build_database(root)
