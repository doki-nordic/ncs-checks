# ncs-checks

Periodically checks things that may affect NCS project.

## How it works

The script `checks/all.py` runs all checks.
If any of the checks need to report something,
the script creates as issue containing the reported information.

The check is a script named `checks/check_*.py`.
If the script wants to report something,
it uses a Jinja2 markdown template from the `templates` directory.
The template will be rendered to a comment in a newly created issue.
The comment contains users mentions to notify interested people.

The check can save some information between each run, e.g.
to avoid reporting the same thing each day.
Files contained in the `data` directory will be preserved.
They will be committed into `data` branch by github's workflow.
If you running the script locally, you have to take care of committing `data` directory manually.

## How to run it locally

1. Set environment variables:
   * `GITHUB_TOKEN` - token that will be used to communicate with the Github API.
   * `GITHUB_ACTOR` - user name responsible for running the script
   * `GITHUB_REPO` - repository (in form `github_user/repository_name`) where a new issue will be created.
1. Clone `data` branch to a `data` directory.
   The state of the cloned repository must be clean (no changes in working directory and index), so revert, commit or stash your changes before running the script.
1. Now you can run:
   * `python checks/all.py` to run all checks and create an issue if needed.
   * `python checks/some_check.py` to run a specific check without creating an issue. The result will be show on terminal.

## How to write a check

1. Create script named `checks/check_*.py`.
1. Put you checking logic in it.
1. Create one or more comment templates in the `templates` directory.
1. Mention all interested people at the beginning of the template.
1. Use a template to report something if needed

## Common module

The `checks/common.py` module provides API to help writing a check.

* `send_notification(template, **data)`

  Send notification using provided `template` and pass `data` to that template.

* `github`

  Instance of PyGithub's main class initialized using `GITHUB_TOKEN` environment variable.
  See: https://pygithub.readthedocs.io/en/latest/github.html

* `github_actor`

  String containing user name that is responsible for running this script (`GITHUB_ACTOR` environment variable).

* `repo`

  Instance of PyGithub's `Repository` class lazy initialized using `GITHUB_REPO` environment variable.
  See: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html


* `data_path` / `templates_path`

  Instance of `Path` class pointing `data` / `templates` directory.

* `class DataDir`

  Helper class for handling the `data` directory.
