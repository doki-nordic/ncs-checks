
import time
import traceback
from pathlib import Path
from common import send_notification, notifications, repo

def _main():
    for check_script in Path(__file__).parent.glob('check_*.py'):
        try:
            __import__(check_script.stem, globals(), locals(), [], 0)
        except BaseException:
            send_notification('script-error.md', script_path=check_script.name, trace=traceback.format_exc())
    if len(notifications) > 0:
        issue = repo.create_issue(f'Notifications from {time.ctime()}', 'I detected some issues that should be addressed.')
        for notification in notifications:
            issue.create_comment(notification)

if __name__ == "__main__":
    _main()
