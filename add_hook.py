import os

import gitlab
import argparse


def project_has_hook(hook_url, project):
    contains_hook = False
    for proj_hook in project.hooks.list():
        if proj_hook.url == hook_url:
            contains_hook = True
            break
    return contains_hook


def add_hook_all_projects(gitlab_url, hook_url, events):
    gl = gitlab.Gitlab(gitlab_url, private_token=os.environ['GITLAB_TOKEN'])

    projects = gl.projects.list(iterator=True)
    for project in projects:
        contains_hook = project_has_hook(hook_url, project)
        if not contains_hook and project.name == "dbz-gohan":
            hook_events = {
                "url": hook_url,
                "push_events": 0,
                "tag_push_events": 0,
                "issue_events": 0,
                "note_events": 0,
                "merge_request_events": 0,
                "wiki_page_events": 0,
                "pipeline_events": 0,
                "job_events": 0,
                "deployment_events": 0,
                "enable_ssl_verification": 0,
            }

            for ev in events:
                hook_events[ev] = 1

            project.hooks.create(hook_events)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Script to add a webhook in all projects in Gitlab",
    )

    parser.add_argument(
        'git_url',
        help='The Gitlab url',
    )

    parser.add_argument(
        'hook_url',
        help='The hook url',
    )

    parser.add_argument(
        'events',
        help='Gitlab hook events as an array',
    )

    args = parser.parse_args()

    add_hook_all_projects(args.git_url, args.hook_url, args.events.split(","))