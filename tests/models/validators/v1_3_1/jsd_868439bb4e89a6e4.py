# -*- coding: utf-8 -*-
"""DNA Center Get Issue Enrichment Details data model.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidator868439Bb4E89A6E4(object):
    """Get Issue Enrichment Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator868439Bb4E89A6E4, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "issueDetails": {
                "description":
                "Issue Details",
                "properties": {
                "issue": {
                "description":
                "Issue",
                "items": {
                "properties": {
                "impactedHosts": {
                "description":
                "Impacted Hosts",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                },
                "issueCategory": {
                "description":
                "Issue Category",
                "type": [
                "string",
                "null"
                ]
                },
                "issueDescription": {
                "description":
                "Issue Description",
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntity": {
                "description":
                "Issue Entity",
                "type": [
                "string",
                "null"
                ]
                },
                "issueEntityValue": {
                "description":
                "Issue Entity Value",
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "issueId": {
                "description":
                "Issue Id",
                "type": [
                "string",
                "null"
                ]
                },
                "issueName": {
                "description":
                "Issue Name",
                "type": [
                "string",
                "null"
                ]
                },
                "issuePriority": {
                "description":
                "Issue Priority",
                "type": [
                "string",
                "null"
                ]
                },
                "issueSeverity": {
                "description":
                "Issue Severity",
                "type": [
                "string",
                "null"
                ]
                },
                "issueSource": {
                "description":
                "Issue Source",
                "type": [
                "string",
                "null"
                ]
                },
                "issueSummary": {
                "description":
                "Issue Summary",
                "type": [
                "string",
                "null"
                ]
                },
                "issueTimestamp": {
                "type": [
                "number",
                "null"
                ]
                },
                "suggestedActions": {
                "description":
                "Suggested Actions",
                "items": {
                "properties": {
                "message": {
                "description":
                "Message",
                "type": [
                "string",
                "null"
                ]
                },
                "steps": {
                "description":
                "Steps",
                "items": {},
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
