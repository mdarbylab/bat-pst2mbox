# ADR 0001: Stack and license

Status: Accepted

## Context

We need to read Outlook PST files and write mbox files that The Bat! imports. No mature pure-Python
or Rust PST parser exists. libpff is the established open parser (LGPLv3+, alpha status).
PstMboxConverter uses `libratom`, which wraps libpff.

## Decision

- Python 3.10+, using libpff's Python bindings.
- Our code is MIT licensed. libpff is LGPL, so it is used as a separately installed, dynamically
  linked dependency and is never vendored.
- Avoid GPL parsers such as readpst/libpst, which would force GPL on this project.

## Consequences

- Fast route to a working tool.
- A packaged Windows build will be larger and may trigger antivirus false positives.
- Bundling libpff in a release must ship its LGPL notice and let users replace it.
- Open question for the spike: which libpff binding installs cleanly on Windows with current Python.
