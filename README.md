# add-hook-all-projects
The goal of this project is to create a webhook for all projects in Gitlab.

## Dependencies
This project uses `python-gitlab`. If you don't have it installed in your machine, you can install it using the following command:
```shell
pip install python-gitlab
```

## How to use
To execute this script you must set the environment variable `GITLAB_TOKEN` having the Gitlab Token to allow performing operations in Gitlab.

Example of usage:
```shell
python add-hook-all-projects http://gitlab.domain.io https://hook_url/hooks job_events,pipeline_events,deployment_events
```


