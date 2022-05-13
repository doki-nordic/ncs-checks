
from common import DataDir, send_notification, github

data_dir = DataDir('spdx')

version = github.get_repo('spdx/license-list-data', lazy=True).get_latest_release().tag_name

data_dir.write_file('latest.txt', version)

if data_dir.changed():
    send_notification('spdx-license-list.md', version=version)
