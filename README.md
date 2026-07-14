# omsp-website

Public standards website for **OMSP (Open Maritime Systems Platform)**:
<https://omsp-foundation.github.io/omsp-website/>

This repository is a **derived publication surface** governed by
[ADR-0003](https://github.com/OMSP-Foundation/omsp-bootstrap/blob/develop/governance/ADR-0003-PUBLIC-STANDARDS-WEBSITE.md).
It contains only the site shell: theme/configuration (`mkdocs.yml`),
site-authored landing pages (`docs/`), the content-sync script
(`scripts/sync_content.py`) and CI. **No governed standards content lives
here** — the single source of truth is
[`omsp-bootstrap`](https://github.com/OMSP-Foundation/omsp-bootstrap).

## How publication works

At build time (`.github/workflows/deploy.yml`):

1. `omsp-bootstrap` is checked out read-only at two refs:
   the newest non-draft release tag (**stable / latest**) and `develop`
   (**dev**, clearly pre-release).
2. `scripts/sync_content.py` copies only Markdown artifacts whose front
   matter carries `Classification: Public` into `docs/standards/`.
3. [`mike`](https://github.com/jimporter/mike) deploys each channel as a
   version to the `gh-pages` branch; GitHub Pages serves it.

Rebuild triggers: `repository_dispatch` (`omsp-content-updated`) sent by
`omsp-bootstrap` on every `develop` merge and release publication, plus a
weekly cron and manual `workflow_dispatch` as safety nets.

## Local preview

```bash
pip install -r requirements.txt
git clone --depth 1 --branch develop \
  https://github.com/OMSP-Foundation/omsp-bootstrap _source_dev
python scripts/sync_content.py _source_dev docs/standards
mkdocs serve
```

## Governance

Editorial stewardship: the advisory `omsp-web-steward` agent (defined in
`omsp-bootstrap`, `.claude/agents/omsp-web-steward.md`). All decisions —
publication scope, domain, repository settings — belong to the human
maintainer. Content on the site is engineering documentation, not
operational guidance.
