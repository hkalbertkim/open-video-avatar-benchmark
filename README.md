# Open Video Avatar Benchmark

Open Video Avatar Benchmark is a reproducible benchmark harness and landscape study for publicly available video avatar models, including talking-head, audio-driven portrait, semi-body, full-body, gesture, and real-time conversational avatar systems.

## Core Benchmark Question

Are current open-source and publicly runnable avatar models ready for real-time conversational presence?

## Scope

This repository tracks public or publicly runnable video avatar systems, records reproducibility metadata, and provides a safe harness for staged benchmark execution. It is intended for landscape analysis, structured comparison, and paper-grade reporting across talking-head, portrait animation, semi-body, full-body, gesture, and conversational avatar model families.

## Goals

- Maintain a candidate registry with reproducibility, license, weights, input, output, and execution metadata.
- Provide placeholder adapters that can later be expanded into reproducible benchmark runners.
- Support both successful runs and failed or blocked candidates as first-class results.
- Capture failure modes, runtime notes, human-likeness review criteria, and paper appendix material.
- Keep benchmark inputs and generated outputs governed by clear permission and consent rules.

## Non-Goals

- Redistributing third-party datasets, model weights, checkpoints, YouTube clips, identity-bearing media, or proprietary assets.
- Declaring winners before reproducible evidence has been collected.
- Replacing original model licenses, terms, installation instructions, or safety policies.
- Providing production identity-cloning tooling or non-consensual likeness generation workflows.

## Benchmark Dimensions

- Installation and dependency reproducibility
- Weight and license availability
- Official sample smoke-test behavior
- Standard benchmark input behavior
- Runtime and hardware characteristics
- Output integrity and corruption checks
- Lip sync, facial realism, gaze, expression, motion, gesture, and long-duration consistency
- Conversational presence, including listening behavior and turn-taking suitability

## Candidate Status Labels

- `PASS_VIVIDO_INPUT`: custom benchmark input pass
- `PASS_SAMPLE_ONLY`: official sample succeeds, but custom benchmark inputs are not yet verified
- `PATCHED_PASS`: succeeds after documented benchmark-side or local compatibility patches
- `BLOCKED_WEIGHTS`: required weights are unavailable, gated, missing, or unresolved
- `BLOCKED_LICENSE`: license terms prevent benchmark use or publication
- `BLOCKED_DEPENDENCY`: install or runtime dependency prevents execution
- `BLOCKED_HARDWARE`: required hardware is unavailable or insufficient
- `FAIL_OUTPUT_CORRUPTED`: output is generated but malformed, broken, unreadable, or visibly corrupted
- `FAIL_TOO_SLOW`: runtime is too slow for the target real-time conversational setting
- `RETEST_REQUIRED`: prior result is stale, inconclusive, or requires a controlled rerun

## Paper Direction

Working paper title:

**Beyond Lip Sync: A Systematic Landscape and Benchmark of Open Video Avatar Models for Conversational Presence**

The paper will focus on candidate collection methodology, model taxonomy, staged benchmark execution, reproducibility gaps, failure modes, conversational presence evaluation, and recommended modular architecture for future avatar systems.

## Repository Safety, Data, and Model Policy Summary

This repository is a benchmark harness and landscape-study repository. It does not redistribute third-party datasets, third-party model weights, YouTube clips, identity-bearing source videos, license-restricted assets, or generated outputs based on non-permitted likenesses. Candidate models remain governed by their original licenses and terms. Public examples must use owned, explicitly licensed, synthetic, public-domain, or otherwise permitted media.

## Current Status

This is the initial benchmark harness skeleton. Adapters and scripts currently use safe dry-run behavior and do not clone repositories, download weights, run heavy inference, or redistribute assets.
