#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone


def lambda_handler(event, context):
    """Sample pure Lambda function"""

    print(f"Hello! {str(datetime.now(tz=timezone.utc))}")
    return


if __name__ == "__main__":
    lambda_handler(None, None)
