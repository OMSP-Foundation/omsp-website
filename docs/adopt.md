# Adopting OMSP

OMSP is open: anyone may read, evaluate and apply the standard. This page
describes the honest starting points at the current maturity level.

!!! note "Maturity"
    OMSP is a v0.5.x **pre-release** program. The governance and
    engineering framework is mature; the maritime domain content (MODS
    Specification, vessel models, scenarios) is being built now. Adopting
    today means adopting an engineering method and tracking a standard as
    it forms.

## What you can use today

1. **The engineering method** — knowledge-first, model-driven, traceability
   by design. The methodology inventory, engineering playbook, artifact
   metadata standard and validation framework are Active and reusable for
   any systems-engineering documentation program.
2. **The artifact model** — governed Markdown with machine-checked YAML
   front matter (`Artifact-ID`, `Title`, `Version`, `Status`, `Owner`,
   traceability links), validated by open Python tooling.
3. **The MODS stack design** — the layered documentation architecture
   (specification → diagrams → core manual → vessel module → scenarios →
   QRH) as a blueprint for operations documentation.

## What is coming

The maritime ontology, MODS Specification v0.1 (ODS series) and the first
Vessel Definition Module (Hanse 460, electrical system golden path) are the
current development horizon. Watch the
[roadmap](https://github.com/OMSP-Foundation/omsp-bootstrap/issues) and the
release feed.

## Ground rules for adopters

- Treat everything with status **Draft** or **Review** as unstable.
- Cite the standard by release version (use the site's **latest** channel,
  not **dev**).
- Nothing here is operational guidance; validation against a real vessel is
  the adopter's responsibility and OMSP's safety boundaries apply.
