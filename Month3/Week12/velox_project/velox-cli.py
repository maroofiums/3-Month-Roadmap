#!/usr/bin/env python3
"""
Velox CLI - Command Line Interface
"""
import sys
import os

# Add parent directory to path to allow importing velox
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from velox.cli.main import main

if __name__ == '__main__':
    main()
