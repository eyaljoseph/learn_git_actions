#!/bin/bash
set -e

# Check if any arguments are provided (likely for ggshield)
if [ "$#" -gt 0 ]; then
  # Run ggshield with the provided arguments
  ggshield "$@"
else
  # If no arguments, run your Flask application
  exec python main.py
fi