# bat-pst2mbox

A free, open-source converter from Outlook `.pst` files to `.mbox`, built for importing mail into
[The Bat!](https://www.ritlabs.com/). One of mdarbylab's few FOSS projects.

> **Status: pre-alpha.** Nothing converts yet. This repository is the phase 0 scaffold.

## Goals

- Write **one mbox per PST folder**, in a directory tree that mirrors the PST, because The Bat!
  imports one mbox per folder (*Tools | Import Messages | From UNIX mailboxes*).
- Never lose mail: the PST is opened read-only, every skipped or corrupt item is logged, and a
  summary of counts in versus counts out is printed at the end.
- Faithful MIME: text and HTML bodies, inline images, attachments, real Date and Message-ID headers.
- Windows first, with a CLI first and a small GUI later.

## Non-goals

- Reading The Bat!'s native `.tbb` format, or writing PSTs.
- Cloud or webmail upload.

## Inspiration

[PstMboxConverter](https://github.com/Jerome2606/PstMboxConverter) (MIT) showed the PST to mbox path.
This is an independent implementation with a different output layout.

## Stack

Python 3.10+, [libpff](https://github.com/libyal/libpff) (LGPLv3+) through its Python bindings,
linked dynamically. Our own code is MIT licensed. See `docs/adr/0001-stack-and-license.md`.

## Development

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows; use .venv/bin/activate elsewhere
pip install -e ".[dev]"
pytest
```

## Roadmap

0. Scaffold (this)
1. Spike: read a PST, write one mbox, test the import in The Bat!
2. Core converter
3. CLI hardening
4. GUI and Windows packaging
5. v0.1 release

## License

MIT. See `LICENSE`.
