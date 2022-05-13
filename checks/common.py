
import os
import tempfile
import yaml
from pathlib import Path
from github import Github
from types import SimpleNamespace


def write_output(markdown, group):
    output = f'{groups[group]}\n\n---\n\n{markdown}'
    print('==================================================================================')
    print(output)
    print('==================================================================================')
    with open(tempfile.mkstemp(suffix='.md', prefix='', dir=output_path, text=True)[0], mode='w') as f:
        f.write(output)

def get_data_dir(subdir):
    my_data_dir = data_path / subdir
    my_data_dir.mkdir(parents=True, exist_ok=True)
    return my_data_dir

def _read_groups():
    with open(Path(__file__).parent.parent / 'groups.yaml', 'r') as f:
        return yaml.safe_load(f)

github = Github(os.environ['GITHUB_TOKEN'])
print(f'Github API connected. Remaining requests {github.rate_limiting[0]} of {github.rate_limiting[1]}.')
github_actor = os.environ['GITHUB_ACTOR']
repo = github.get_repo(os.environ['GITHUB_REPO'], lazy=True)
data_path = (Path(__file__).parent.parent / 'data').resolve()
output_path = (Path(__file__).parent.parent / 'output').resolve()
groups = _read_groups()

data_path.mkdir(exist_ok=True)
output_path.mkdir(exist_ok=True)
