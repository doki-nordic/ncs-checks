
from common import get_data_dir, send_notification, github

my_tag_file = get_data_dir('spdx') / 'latest.txt'

new_tag = github.get_repo('spdx/license-list-data', lazy=True).get_latest_release().tag_name
try:
    old_tag = my_tag_file.read_text()
except:
    old_tag = ''

if new_tag != old_tag:
    send_notification('spdx-license-list.md', version=new_tag)
    my_tag_file.write_text(new_tag)
