# Open Maritime Systems Platform

**OMSP** is an open standard for **knowledge-first, model-driven maritime
systems engineering**. It defines how a vessel's systems, operating
knowledge and procedures are captured as governed, traceable, plain-text
engineering artifacts — and how human-readable operations documentation is
derived from that single model.

The reference vessel for the program is the **Hanse 460** sailing yacht,
developed toward a digital-twin target.

!!! warning "Engineering documentation — not operational guidance"
    Everything published here is engineering documentation of an evolving
    standard. Nothing on this site is an operational instruction, a
    certification, or a statement of seaworthiness. Artifact lifecycle
    statuses (**Draft / Review / Active**) are published exactly as they
    stand in the source repository.

## The MODS product stack

OMSP's core product is the **Maritime Operations Documentation Standard
(MODS)** — a layered, spec-first documentation stack adapted from aviation
operational-documentation practice (AFM, FCOM, SOP, QRH):

| Layer | What it is |
| --- | --- |
| MODS Specification (ODS-100…600) | The vessel-agnostic documentation standard |
| Marine Diagram System | Text-based, generatable diagram sources |
| Core Operations Manual | Vessel-class operating documentation |
| Vessel Definition Module | Per-vessel delta content (first: Hanse 460) |
| Scenario Library | Traceable operational scenarios |
| QRH | Quick Reference Handbook, derived from procedures |

Each layer is produced only when the layer above it is at least a governed
Draft — the YAML model is the single source; publications are derived.

## Read the standards

The full governed artifact set — canon, governance, ontology, schemas,
reference models and validation framework — is published under
**Standards** in the navigation, synced automatically from the
[omsp-bootstrap](https://github.com/OMSP-Foundation/omsp-bootstrap)
repository:

- **stable** (`latest`) — the most recent release,
- **dev** — the current `develop` branch, clearly pre-release.

Use the version selector in the header to switch channels.

## Where the program stands

OMSP is in active early development (v0.5.x pre-release line). The clean
baseline is done; the current horizon builds the first real maritime domain
value: the maritime ontology, MODS Specification v0.1, and the Hanse 460
electrical golden path. See the roadmap artifacts under Standards for
detail.

## Get involved

- [How to adopt OMSP](adopt.md)
- [How to contribute](contribute.md)
- [Source repository on GitHub](https://github.com/OMSP-Foundation/omsp-bootstrap)
