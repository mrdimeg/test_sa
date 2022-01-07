# Git

## Git actions

```yaml
name: CI

on: [push]

jobs:
  build:
    
    runs-on: ubuntu-latest
    steps:
    - run: echo "The ${{ github.repository }} will be cloned to the runner."
    - uses: actions/checkout@v1
    - name: Run a one-line script
      run: ls -l
    - name: Run a multi-line script
      run: |
        env
        date
