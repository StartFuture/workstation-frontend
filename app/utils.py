import os
from functools import wraps
from flask import session, redirect, Blueprint, render_template, url_for
import requests

import parameters

def clean_str(value):
    value = str(value).strip()
    value = value.replace('.', '').replace(',', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    return value