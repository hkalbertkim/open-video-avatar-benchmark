# Benchmark Protocol

The benchmark uses a staged process so failures, blocks, and partial successes remain interpretable.

1. Candidate intake
2. Official sample smoke test
3. Standard input test
4. Runtime metrics
5. Human-likeness review
6. Failure classification
7. Paper-grade appendix

Each stage should record source commit, environment, command plan, inputs, output paths, runtime, hardware, license constraints, and failure classification. Heavy execution is not part of the initial skeleton.

## Generated Metadata Reports

Reports `00_candidate_inventory.md`, `01_reproducibility_matrix.md`, and `02_license_and_weights_matrix.md` are generated from `candidates/candidates.yaml` by `scripts/update_reports.py`. Update candidate metadata first, then rerun the generator. Do not manually edit those generated reports unless the generator is updated in the same change.
