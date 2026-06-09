# License and Weights Matrix

Generated: 2026-06-09T01:46:51Z

Source file: `candidates/candidates.yaml`

This repository does not redistribute third-party weights, checkpoints, datasets, source videos, identity-bearing media, or restricted generated outputs.

Candidate models remain governed by their original licenses and terms. The repository license applies only to benchmark harness code and documentation authored here.

| id | license | weights source/status | redistribution note | commercial/use caution | remaining CHECK_REQUIRED fields |
| --- | --- | --- | --- | --- | --- |
| musetalk | MIT | AVAILABLE_PUBLIC; https://huggingface.co/TMElyralab/MuseTalk | Do not redistribute MuseTalk or dependency weights from this benchmark repo. | Official README states code is MIT and trained model is commercially available, but third-party component licenses and test-data terms must be checked separately. | Third-party component licenses and test-media terms need per-run review. |
| wav2lip | NON_COMMERCIAL_RESEARCH_PERSONAL_ONLY | AVAILABLE_PUBLIC_LINKED; Google Drive links from official README; face detector weight link also listed. | Do not redistribute Wav2Lip checkpoints or face detector weights. | Official README says open-source results should be research/academic/personal only and commercial use is strictly prohibited because models are trained on LRS2. | Claimed runtime or real-time support was not verified from official source. |
| liveportrait | MIT_WITH_INSIGHTFACE_NONCOMMERCIAL_MODEL_CAUTION | AVAILABLE_PUBLIC; Hugging Face KlingTeam/LivePortrait, Google Drive, and Baidu Yun links from official README. | Do not redistribute LivePortrait pretrained weights or included third-party model files. | LICENSE notes InsightFace models are non-commercial research only and should be removed/replaced for commercial use. | Training code availability remains unverified from official source. |
| ditto | Apache-2.0 | AVAILABLE_PUBLIC; https://huggingface.co/digital-avatar/ditto-talkinghead | Do not redistribute Ditto checkpoints, ONNX files, TensorRT engines, or PyTorch weights from this benchmark repo. | Apache-2.0 repository license verified; auxiliary model/checkpoint terms still need review before publishing benchmark outputs. | Auxiliary model and checkpoint terms need review before benchmark publication. |
| echomimic | Apache-2.0 | AVAILABLE_PUBLIC; https://huggingface.co/BadToBest/EchoMimic | Do not redistribute EchoMimic checkpoints or dependency weights. | Demo-image provenance note in README means examples should not be reused as benchmark assets without independent permission. | V1 training code was not verified from official README. |
| hallo2 | MIT_WITH_SLAB_HIGH_RES_CAUTION | AVAILABLE_PUBLIC; https://huggingface.co/fudan-generative-ai/hallo2 | Do not redistribute Hallo2 pretrained models or third-party component weights. | GitHub shows MIT license, but README states the high-resolution feature is modified from CodeFormer and subject to S-Lab License 1.0. | No real-time claim verified; high-resolution feature license terms need review before redistribution or publication. |
