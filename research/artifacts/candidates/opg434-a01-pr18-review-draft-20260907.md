# PR 18 paper self-review — NOT SUBMITTED

verdict: candidate_only
repository: vibemathing/problem-opg-434-weak-pentagon
issue: 3
pull_request: 18
base_revision: d8220b87d903640d1abd2d835aba2f01a32f23dc
reviewed_head: 7d278210fe9f751b260b6f5a10584273375a468c
review_status: local draft only

## Read surface

The complete three-file changed-path list was retrieved. The C15 proof and
checkpoint patches were read. The final packet binding was read in the
exact-head commit diff, including PR 18 and Issue 3, the admitted identities,
base, requested capabilities and candidate digest. All three changed paths
are within the admitted candidate/inbox surface.

## Mathematical audit

The child-list recurrence uses union neighborhoods before intersection and
includes attainment. The two prescribed root lists have disjoint neighborhood
unions, which is an obstruction to the extra punctured-map repair rule.
The positive one-port graph is an edge-subdivided pair-disjointness graph:
the changed image at source vertex 12 and the new subdivision vertex satisfy
all affected target edges. A five-cycle avoiding that subdivision proves
exact girth five. Each added attachment is a bridge, so original tree
distances are preserved. The gadget attached at the removed vertex remains
a separately mapped component; no missing image was silently assumed.

The full positive map and the obstructed punctured map are different maps.
The proof therefore does not assert root nonexistence. The bridge limitation
is explicitly stated. No paper defect was identified in this review, but
this is generator review, not a trusted mathematical verifier result.

## Observed transport checks

Exact head: 7d278210fe9f751b260b6f5a10584273375a468c
Run: 34066189251
- web-pr-diff-boundary: success; job 101575244655
- web-harness-snapshot: success; job 101575244715
- web-attempt-packet: success; job 101575244777

The most recent PR read reported open, merged=false, mergeable=true, with
the same head. The merge_commit_sha returned for an OPEN PR is not treated
as evidence of a completed merge. No merge action was available in the
exposed GitHub tool catalog; no merge or submitted review is claimed here.

## New nonduplicate preparation

The layered pentagon candidate supplies stronger auxiliary negative
knowledge without altering this PR: it removes bridges and nontrivial
three-edge cuts and treats an induced pentagon hole, not just one missing
vertex. It also proves a lower bound on the count of changed old vertex labels.
It has a separate explicit total map and a genuine exterior map.

Next transport must start with a fresh read of PR 18/main. Never overwrite
the existing C15 packet with this preparation or recreate Issue 3.
