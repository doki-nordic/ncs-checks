
from common import get_data_dir, write_output, github

my_tag_file = get_data_dir('spdx') / 'latest.txt'

new_tag = github.get_repo('spdx/license-list-data', lazy=True).get_latest_release().tag_name
try:
    old_tag = my_tag_file.read_text()
except:
    old_tag = ''

comment_text = f'''
Newer version `{new_tag}` of SPDX license list detected.

Update `west ncs-sbom` tool:
* [ ] Run: `python nrf/scripts/west_commands/sbom/helpers/update_spdx_licenses.py`
* [ ] Commit and push changes of the `nrf/scripts/west_commands/sbom/data/spdx-licenses.yaml` file
* [ ] Create a PR
'''

if new_tag != old_tag:
    write_output(comment_text, 'spdx')
    my_tag_file.write_text(new_tag)
