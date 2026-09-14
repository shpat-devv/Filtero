#!/usr/bin/env bash

set -e

echo "Cleaning up..."

echo "Removing Python cache files..."
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete

echo "Removing Python tooling caches..."
rm -rf .pytest_cache
rm -rf .mypy_cache
rm -rf .ruff_cache

echo "Removing Python virtual environments..."
rm -rf .venv
rm -rf venv
rm -rf env
rm -rf ENV

echo "Removing Django generated files..."
rm -rf staticfiles
rm -rf media

echo "Removing local SQLite database..."
rm -f db.sqlite3
rm -f db.sqlite3-journal

echo "Removing node_modules..."
find . -type d -name "node_modules" -prune -exec rm -rf {} +

echo "Removing frontend build files..."
rm -rf frontend/dist
rm -rf frontend/build
rm -rf frontend/.vite

echo "Removing TypeScript build cache..."
find . -type f -name "*.tsbuildinfo" -delete

echo "Removing coverage files..."
rm -rf coverage
rm -rf .nyc_output

echo "Removing npm/yarn/pnpm logs..."
find . -type f \( \
    -name "npm-debug.log*" \
    -o -name "yarn-debug.log*" \
    -o -name "yarn-error.log*" \
    -o -name "pnpm-debug.log*" \
\) -delete

echo "Removing OS generated files..."
find . -type f \( \
    -name ".DS_Store" \
    -o -name "Thumbs.db" \
    -o -name "Desktop.ini" \
\) -delete

echo "Removing editor temporary files..."
find . -type f \( \
    -name "*.swp" \
    -o -name "*.swo" \
    -o -name "*~" \
\) -delete

echo "Removing Jupyter cache..."
find . -type d -name ".ipynb_checkpoints" -prune -exec rm -rf {} +

echo "Removing project specific files..."
rm backend/uploads/*

echo "Cleanup complete"
