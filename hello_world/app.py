#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
import json


def lambda_handler(event, context):
    """Sample pure Lambda function"""

    print(f"Hello! {str(datetime.now(tz=timezone.utc))}")
    print(json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "event": event,
            }
        ),
    }


if __name__ == "__main__":
    lambda_handler(None, None)
