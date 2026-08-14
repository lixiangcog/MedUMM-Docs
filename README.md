# MedUMM Documentation

This repository is the independently versioned documentation site for
[MedUMM](https://github.com/lixiangcog/MedUMM), a unified medical multimodal
model toolkit.

Published site: <https://lixiangcog.github.io/MedUMM-Docs/>

The site has two primary reading paths:

- **Understand MedUMM** — concepts, architecture, workflows, validation levels,
  and current limitations in plain language.
- **Build MedUMM** — project requirements, interfaces, extension guides, CLI,
  configuration, operations, and release evidence.

## Build locally

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r docs/requirements.txt
.venv/bin/sphinx-build -W --keep-going -b html docs _build/html
```

Open `_build/html/index.html` after the build completes.

## Publishing

The repository is ready for Read the Docs through `.readthedocs.yaml`. Import
the GitHub repository in Read the Docs and keep the configuration-file path at
its root default. A GitHub Pages workflow is also included as a deployable
fallback.

## Source of truth

Platform behavior and release evidence are verified against MedUMM `v1.4.0`.
When code and prose differ, the pinned MedUMM source and machine-readable
release evidence take precedence. Documentation updates should name the code
release they describe.

MedUMM is research software, not a medical device.
