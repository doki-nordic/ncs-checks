
import os
import subprocess
import tempfile
from pathlib import Path
from github import Github
from jinja2 import Template


def send_notification(template, **data):
    t = Template((templates_path / template).read_text())
    output = t.render(data)
    print('============================= BEGIN NOTIFICATION =============================')
    print(output)
    print('============================== END NOTIFICATION ==============================')
    with open(tempfile.mkstemp(suffix='.md', prefix='', dir=output_path, text=True)[0], mode='w') as f:
        f.write(output)

class DataDir:

    def __init__(self, subdir='common'):
        self.path = data_path / subdir
        self.path.mkdir(parents=True, exist_ok=True)

    def read_file(self, file_name, default_content=None):
        file = self.path / file_name
        if not file.exists() and default_content is not None:
            file.write_text(default_content)
        return file.read_text()

    def write_file(self, file_name, content):
        file = self.path / file_name
        file.write_text(content)

    def changed(self):
        cp = subprocess.run(['git', 'status',  '--porcelain', '.'], cwd=self.path, capture_output=True)
        if len(cp.stderr):
            print(cp.stderr)
            raise Exception('Command shows an error message!')
        if cp.returncode != 0:
            raise Exception(f'Command returned exit status {cp.returncode}!')
        return len(cp.stdout.strip()) != 0


github = Github(os.environ['GITHUB_TOKEN'])
print(f'Github API connected. Remaining requests {github.rate_limiting[0]} of {github.rate_limiting[1]}.')
github_actor = os.environ['GITHUB_ACTOR']
repo = github.get_repo(os.environ['GITHUB_REPO'], lazy=True)
data_path = (Path(__file__).parent.parent / 'data').resolve()
output_path = (Path(__file__).parent.parent / 'output').resolve()
templates_path = (Path(__file__).parent.parent / 'templates').resolve()

data_path.mkdir(exist_ok=True)
output_path.mkdir(exist_ok=True)
