#!/usr/bin/env python3

from app import app
from app.controllers import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)