#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: slug.py
Author: Daniel Schneider
Date: 01/03/2024
Description: This file produces a slug name.
"""

from coolname import generate_slug
import random

print(f"{generate_slug(2)}-{random.randint(1,100)}")