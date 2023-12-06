# LaunchFlow actions-promote

A GitHub action for promoting deployments between [environments](https://docs.launchflow.com/launchflow-cloud/user-guides/environments) in LaunchFlow. This action can be used to promote a deployment running in one environment to another. For instance you can use this action to promote a deployment running in the `dev` environment to the `prod` environment.

## Prerequisites

- Create a [LaunchFlow project](https://docs.launchflow.com/launchflow-cloud/user-guides/projects)
- Create [two environments]((https://docs.launchflow.com/launchflow-cloud/user-guides/environments)) in your LaunchFlow project
- [Launch a deployment](](https://docs.launchflow.com/launchflow-cloud/user-guides/create-a-deployment) ) in the environment you are promoting from

## Usage

The below is an example from promoting from a `dev` environment to a `prod` environment. This will take the deployment running in the `dev` environment and launch in in the `prod` environment. You need to provide the environment names, the deployment key for the `prod` environment, and the project ID the environments live in. We recommend storing the project ID and deployment key as secrets in your repository.

```yaml
on:
  workflow_dispatch:

name: Release Prod
concurrency: prod
jobs:
  release-prod:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: "write"
    environment: prod
    steps:
      - uses: "actions/checkout@v3"

      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Promote to Prod
        uses: launchflow/actions-promote@v1
        with:
          project_id: ${{ secrets.LAUNCHFLOW_PROJECT_ID }}
          from_environment_name: dev
          to_environment_name: prod
          deployment_key: ${{ secrets.LAUNCHFLOW_PROD_DEPLOYMENT_KEY }}

```

## Configuration

| Input                 | Description                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project_id            | The LaunchFlow project to deploy to. Should be of the format `project_XXXXXX`                                                                                       |
| from_environment_name | The environment in the project that you are promoting from (from -> to). This should match the name you provided when you created your environment (e.g. `dev`)     |
| to_environment_name   | The environment in the project that you are promoting to (from -> to). This should match the name you provided when you created your environment (e.g.  `prod` )    |
| deployment_key        | The LaunchFlow deployment key of the environment you are promoting **to** use for authentication. This key is initially generated when you create your environment. |
| launchflow_cli_version        | The version of the LaunchFlow CLI to use. Defaults to the latest version. |
