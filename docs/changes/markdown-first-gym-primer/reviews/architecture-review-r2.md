# Architecture Review R2: AI Raster Media Provenance

## Result

- Review surface: canonical-architecture-update and ADR
- Review status: changes-requested
- Material findings: AR-MEDIA-1
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/markdown-first-gym-primer/reviews/architecture-review-r2.md`
- Review log: `docs/changes/markdown-first-gym-primer/review-log.md`
- Review resolution: `docs/changes/markdown-first-gym-primer/review-resolution.md`
- Open blockers: AR-MEDIA-1
- Required canonical updates: define deterministic raster-media
  classification for provenance validation
- Required ADR updates: define the same classification rule or link to it
- Next stage: architecture revision

## Review inputs

- Architecture package:
  `docs/architecture/system/architecture.md`
- Container diagram:
  `docs/architecture/system/diagrams/container.mmd`
- ADR under review:
  `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`
- Related ADR:
  `docs/adr/2026-06-27-markdown-first-citation-based-authority.md`
- Approved spec:
  `specs/markdown-first-primer.md`
- Spec review:
  `docs/changes/markdown-first-gym-primer/reviews/spec-review-r3.md`

## Findings

### AR-MEDIA-1 - Raster media classification is not deterministic

Finding: The architecture requires provenance for AI-generated raster media but
does not define how validation determines that a referenced image is a raster
asset requiring provenance before the provenance row exists.

Location:

- `docs/architecture/system/architecture.md`, Runtime View,
  media validation flow.
- `docs/architecture/system/architecture.md`, Crosscutting Concepts, Media.
- `docs/adr/2026-06-28-ai-generated-raster-media-provenance.md`,
  Decision and Consequences.

Severity: material

Evidence:

- The media validation flow says "If the referenced asset is an AI-generated
  raster illustration" before normalizing and checking `asset_path`, but it
  does not define a deterministic classifier for that condition.
- Crosscutting media rules say AI-generated raster illustrations require a
  centralized provenance row, but they do not state whether raster extensions
  such as `.png`, `.jpg`, `.jpeg`, or `.webp` are always treated as
  AI-generated raster assets in v0.1.
- The ADR consequences say validators must distinguish original SVGs from
  AI-generated raster assets, but the decision does not state the rule that
  makes that distinction.

Required outcome:

- The architecture and ADR must define a deterministic v0.1 media
  classification rule that validation can implement without relying on an
  already-existing provenance row.
- The rule must preserve the approved spec boundary: text-only pages remain
  valid, original SVGs remain allowed, AI-generated raster images require
  `media/PROVENANCE.md`, and third-party or undocumented raster media remain
  out of scope.

Safe resolution path:

- Update the canonical architecture Runtime View and Crosscutting Concepts to
  state that, for v0.1 promoted pages, original educational diagrams are SVG
  assets, and raster image references under `media/` are treated as
  AI-generated raster illustrations requiring provenance.
- Update the media ADR Decision with the same rule, including the covered
  raster extensions or an explicit extension allowlist.
- Route the revised architecture and ADR back to architecture-review R3.
- If the project wants original raster drawings or photos to be allowed without
  AI provenance, route back to spec because that changes the approved media
  contract and validation boundary.

## Review dimensions

- Spec alignment: concern. The design matches R41-R53 in intent, but
  AR-MEDIA-1 leaves a path where a raster image could avoid provenance
  classification.
- Package shape: pass. The canonical package keeps lifecycle metadata, all
  arc42 sections, C4 context/container diagrams, ADR links, risks, quality
  requirements, and glossary.
- Boundary clarity: concern. The media/provenance containers are visible, but
  the boundary between SVG diagrams and provenance-required raster assets needs
  deterministic wording.
- Data ownership: pass. Markdown owns content; `media/PROVENANCE.md` owns AI
  raster provenance; generated HTML remains derived.
- Interface safety: concern. `asset_path` compatibility is covered, but media
  type classification must become an explicit validation contract.
- Runtime and failure handling: concern. Missing, incomplete, non-approved, and
  mismatched provenance failures are covered after classification; the
  pre-classification step is incomplete.
- Deployment and execution boundaries: pass. No hosted deployment is
  introduced; repository browsing, local checks, and derived mdBook remain the
  only execution boundaries.
- Security/privacy: pass. The design excludes identifying people, private data,
  medical/rehab media, and AI-generated guidance as source of truth.
- Quality and operations: pass. Quality scenarios cover readability,
  traceability, scope safety, media licensing, media provenance, portability,
  privacy, and local-check performance.
- Testing feasibility: concern. Tests can validate provenance rows once
  classification is known; AR-MEDIA-1 is needed to make missing-provenance
  raster fixtures deterministic.
- Complexity discipline: pass. Centralized provenance is appropriate for v0.1
  and avoids sidecar metadata or a media platform.
- ADR quality: concern. The ADR has context, decision, alternatives,
  consequences, and follow-up, but must include deterministic raster/SVG
  classification.
- Plan readiness: block. Planning/test-spec update should not proceed until
  AR-MEDIA-1 is resolved and rereviewed.

## C4, arc42, and ADR checks

- arc42 package: pass with one material media-boundary finding.
- C4 context diagram: pass. No system-context change is required.
- C4 container diagram: pass. The media and provenance containers are visible
  at the right level.
- Component diagram: not required. The missing rule is contractual, not a
  component-boundary problem.
- Deployment diagram: not required. No hosted deployment or runtime
  infrastructure is introduced.
- ADR coverage: concern. The new ADR is the right place for the durable
  provenance decision, but it needs the deterministic classification rule.
- Legacy status: pass. The older structured-platform ADR remains historical
  and does not override the Markdown-first media boundary.

## Recommended changes

Update the architecture and ADR to add a rule like this, adjusted as needed by
the architecture author:

> In v0.1 promoted pages, original educational diagrams are SVG files. Any
> referenced raster image under `media/` with an allowed raster extension is
> treated as an AI-generated raster illustration and must have an approved
> matching row in `media/PROVENANCE.md`. Raster image references without a
> matching approved provenance row fail validation.

The architecture author should also name the allowed raster extensions or state
that the checker owns a fixed extension allowlist.

## Readiness

Architecture-review R2 is changes-requested. No automatic downstream handoff is
allowed. The next stage is `architecture` revision for AR-MEDIA-1, followed by
architecture-review R3.
