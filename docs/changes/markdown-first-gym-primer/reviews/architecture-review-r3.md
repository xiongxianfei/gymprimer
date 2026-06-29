# Architecture Review R3: AI Raster Media Provenance

## Result

- Review surface: canonical-architecture-update and ADR
- Review status: approved
- Material findings: none
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r3.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: none
- Required canonical updates: none before lifecycle normalization
- Required ADR updates: none before lifecycle normalization
- Next stage: architecture status normalization

## Review inputs

- Architecture package:
  `docs/architecture/system/architecture.md`
- ADR under review:
  `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
- Prior review:
  `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r2.md`
- Resolution record:
  `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Approved spec:
  `specs/markdown-first-primer.md`

## Findings

None.

## Finding reconciliation

- Finding ID: AR-MEDIA-1
- Prior status: open from `architecture-review-r2`
- R3 result: resolved
- Evidence: The architecture Runtime View now classifies Markdown image
  references by resolved repository path and lowercase extension before
  provenance lookup. `.svg` files under `media/` are original educational
  diagrams, and `.png`, `.jpg`, `.jpeg`, and `.webp` files under `media/` are
  AI-generated raster illustrations that require approved provenance. The ADR
  records the same extension-based rule.

## Review dimensions

- Spec alignment: pass. The design satisfies R41-R53 without expanding v0.1
  beyond the approved media contract.
- Package shape: pass. The canonical architecture retains lifecycle metadata,
  all arc42 sections, C4 context/container diagrams, ADR links, risks, quality
  requirements, glossary, and readiness.
- Boundary clarity: pass. SVG diagrams, raster assets, provenance ownership,
  and validation responsibilities are now separated deterministically.
- Data ownership: pass. Markdown owns instructional content, SVG owns original
  diagrams, and `media/PROVENANCE.md` owns AI raster provenance.
- Interface safety: pass. `asset_path`, allowed raster extensions, failure
  codes, and extension-based classification are explicit compatibility
  surfaces.
- Runtime and failure handling: pass. The media flow covers classification,
  provenance lookup, missing local files, remote images, paths outside `media/`,
  unsupported extensions, incomplete provenance, and unapproved provenance.
- Deployment and execution boundaries: pass. No hosted deployment, media
  platform, sidecar metadata system, or generated JSON product is introduced.
- Security/privacy: pass. Identifying people, private data, medical/rehab
  media, and AI-generated exercise guidance as source of truth remain excluded.
- Quality and operations: pass. Observability includes classification and
  stable failure codes suitable for deterministic tests.
- Testing feasibility: pass. Missing-provenance raster fixtures are now
  deterministic because classification does not depend on an existing
  provenance row.
- Complexity discipline: pass. The design uses a strict v0.1 extension
  allowlist instead of a broader media taxonomy.
- ADR quality: pass. The ADR records context, decision, alternatives,
  consequences, compatibility, and follow-up.
- Plan readiness: pass after lifecycle normalization. The reviewed design is
  ready for downstream test-spec and plan updates once the architecture package
  and ADR statuses are normalized.

## C4, arc42, and ADR checks

- arc42 package: pass. Required sections are present and current.
- C4 context diagram: pass. No context-level change was needed for AR-MEDIA-1.
- C4 container diagram: pass. Media and provenance containers remain visible at
  the right level.
- Component diagram: not required. The resolved issue is a validation contract,
  not an internal component-boundary problem.
- Deployment diagram: not required. v0.1 still has no hosted deployment or
  runtime infrastructure.
- ADR coverage: pass. The media ADR now records the durable classification and
  provenance decision.
- Legacy status: pass. The older structured-platform ADR remains historical and
  does not override the Markdown-first media boundary.

## Recommended changes

No architecture or ADR content changes are required before status
normalization.

Before downstream artifacts rely on this design, normalize:

- `docs/architecture/system/architecture.md` from `draft` to `approved`.
- `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md` from
  `proposed` to `accepted`.

## Readiness

Architecture-review R3 approves the media provenance architecture update.
This direct review remains isolated: no automatic downstream handoff is
performed. The next stage is architecture status normalization before
test-spec, plan, or implementation updates rely on the media design.
