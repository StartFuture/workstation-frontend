import os
from functools import wraps
from flask import session, redirect, Blueprint, render_template, url_for
import requests

import parameters

