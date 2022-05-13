
import os
import tempfile
import yaml
from pathlib import Path
from github import Github
from jinja2 import Template, filters


def send_notification(template, **data):
    t = Template((templates_path / template).read_text())
    output = t.render(data)
    print('============================= BEGIN NOTIFICATION =============================')
    print(output)
    print('============================== END NOTIFICATION ==============================')
    with open(tempfile.mkstemp(suffix='.md', prefix='', dir=output_path, text=True)[0], mode='w') as f:
        f.write(output)

def get_data_dir(subdir):
    my_data_dir = data_path / subdir
    my_data_dir.mkdir(parents=True, exist_ok=True)
    return my_data_dir

github = Github(os.environ['GITHUB_TOKEN'])
print(f'Github API connected. Remaining requests {github.rate_limiting[0]} of {github.rate_limiting[1]}.')
github_actor = os.environ['GITHUB_ACTOR']
repo = github.get_repo(os.environ['GITHUB_REPO'], lazy=True)
data_path = (Path(__file__).parent.parent / 'data').resolve()
output_path = (Path(__file__).parent.parent / 'output').resolve()
templates_path = (Path(__file__).parent.parent / 'templates').resolve()

data_path.mkdir(exist_ok=True)
output_path.mkdir(exist_ok=True)
