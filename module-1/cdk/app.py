#!/usr/bin/env python3

from aws_cdk import core

from cdk.web_application_stack import WebApplicationStack


app = core.App()
WebApplicationStack(app, "MythicalMysfits-Website")

app.synth()