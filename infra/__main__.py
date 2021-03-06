#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cdp_backend.infrastructure import CDPStack
from pulumi import export

###############################################################################

cdp_stack = CDPStack(
    gcp_project_id="missoula-council-data-proj",
    municipality_name="Missoula",
    firestore_location="us-central",
    hosting_github_url="https://github.com/OpenMontana/missoula-council-data-project",
    hosting_web_app_address="https://OpenMontana.github.io/missoula-council-data-project",
    governing_body="city council",
)

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
