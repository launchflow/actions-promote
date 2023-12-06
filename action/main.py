"""GitHub Action for LaunchFlow Promot."""
import os
import re
import sys
from subprocess import check_call

VERSION = os.getenv("INPUT_VERSION", default="")
FROM_ENVIRONMENT = os.environ["INPUT_FROM_ENVIRONMENT"]
TO_ENVIRONMENT = os.environ["INPUT_TO_ENVIRONMENT"]
PROJECT = os.environ["INPUT_PROJECT_ID"]
DKEY = os.environ["INPUT_DKEY"]
CLI_VERSION = os.getenv("INPUT_CLI_VERSION", None)

if CLI_VERSION is not None:
    cmd = f"pip install launchflow=={CLI_VERSION}"
else:
    cmd = "pip install launchflow"

cmd = "pip install launchflow"
check_call(cmd, shell=True)
cmd = (
    "launch deployments promote-environment "
    f"-t {TO_ENVIRONMENT} -f {FROM_ENVIRONMENT} --project-id={PROJECT} --dkey={DKEY}"
)
check_call(cmd, shell=True)
