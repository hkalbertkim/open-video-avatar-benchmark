# Failure Taxonomy

- Dependency failure: installation or runtime dependency prevents execution.
- Missing weights: required model files are unavailable, gated, missing, or unresolved.
- License block: license or terms prevent benchmark execution or publication.
- Hardware block: required GPU, memory, driver, or accelerator support is unavailable.
- Sample-only success: official sample works, but standard benchmark input is unverified or fails.
- Custom input collapse: model runs but fails on standard benchmark media.
- Identity drift: output identity departs materially from permitted source identity.
- Dead eyes: gaze and eyelid behavior look static, unfocused, or unnatural.
- Gesture repetition: body or hand motion repeats visibly and harms conversational realism.
- Body/hand corruption: limbs, hands, torso, or body shape degrade visibly.
- Too slow for real-time: runtime cannot support target conversational latency.
- Output corrupted: generated file is malformed, unreadable, visually broken, or incomplete.
- Retest required: result is stale, inconclusive, flaky, or lacks sufficient evidence.
