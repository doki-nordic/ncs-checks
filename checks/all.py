
import time
import traceback
from pathlib import Path
from common import send_notification, output_path, repo

def _main():
    for check_script in Path(__file__).parent.glob('check_*.py'):
        try:
            __import__(check_script.stem, globals(), locals(), [], 0)
        except BaseException:
            send_notification('script-error.md', script_path=check_script.name, trace=traceback.format_exc())
    comments = []
    for file in output_path.glob('**/*.md'):
        comments.append(file.read_text())
    if len(comments) > 0:
        issue = repo.create_issue(f'Notifications from {time.ctime()}', 'I detected some issues that should be addressed.')
        for comment in comments:
            issue.create_comment(comment)

if __name__ == "__main__":
    _main()
