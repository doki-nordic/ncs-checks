{# This notification will be send if the SPDX license list version is updated (a new release of the github repository containing the list data). #}

@doki-nordic @maje-emb

---

Newer version `{{ version }}` of the SPDX license list detected.

Update `west ncs-sbom` tool:

* [ ] Run: `python nrf/scripts/west_commands/sbom/helpers/update_spdx_licenses.py`
* [ ] Commit and push changes of the `nrf/scripts/west_commands/sbom/data/spdx-licenses.yaml` file
* [ ] Create a PR
