
from common import DataDir, send_notification, github

data_dir = DataDir('spdx')

new_tag = github.get_repo('spdx/license-list-data', lazy=True).get_latest_release().tag_name
old_tag = data_dir.read_file('latest.txt', '')

if new_tag != old_tag:
    send_notification('spdx-license-list.md', version=new_tag)
    data_dir.write_file('latest.txt', new_tag)
