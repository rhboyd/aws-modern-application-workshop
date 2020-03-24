#!/usr/bin/env python3

from aws_cdk import core

from cdk.web_application_stack import WebApplicationStack
from cdk.network_stack import NetworkStack


app = core.App()
WebApplicationStack(app, "MythicalMysfits-Website")
networkstack = NetworkStack(app, "MythicalMysfits-Network")

app.synth()