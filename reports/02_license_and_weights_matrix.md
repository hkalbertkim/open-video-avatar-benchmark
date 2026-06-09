# License and Weights Matrix

Metadata verification timestamp: 2026-06-09 Asia/Seoul.

Source policy: license and weights fields are based on official public sources where possible: candidate GitHub repositories, official READMEs, official model cards, and paper/arXiv pages. This repository does not redistribute third-party weights, checkpoints, datasets, source videos, identity-bearing media, or restricted generated outputs.

| Candidate | License | Weights Source | Redistribution Note | Caution Note |
| --- | --- | --- | --- | --- |
| musetalk | MIT | https://huggingface.co/TMElyralab/MuseTalk plus third-party component sources listed in official README | Do not redistribute MuseTalk or dependency weights from this benchmark repo. | Official README states code is MIT and trained model is commercially available, but third-party component licenses and test-data terms must be checked separately. |
| wav2lip | NON_COMMERCIAL_RESEARCH_PERSONAL_ONLY | Official README links Google Drive checkpoints and a face detector model. | Do not redistribute Wav2Lip checkpoints or face detector weights. | Official README says all open-source outputs should be research/academic/personal only and commercial use is strictly prohibited because the models are trained on LRS2. |
| liveportrait | MIT_WITH_INSIGHTFACE_NONCOMMERCIAL_MODEL_CAUTION | Hugging Face `KlingTeam/LivePortrait`, Google Drive, and Baidu Yun links from official README. | Do not redistribute LivePortrait pretrained weights or included third-party model files. | LICENSE notes InsightFace models are non-commercial research only and should be removed/replaced for commercial use. |
| ditto | Apache-2.0 | https://huggingface.co/digital-avatar/ditto-talkinghead | Do not redistribute Ditto checkpoints, ONNX files, TensorRT engines, or PyTorch weights from this benchmark repo. | Apache-2.0 repository license verified; auxiliary model/checkpoint terms still need review before publishing benchmark outputs. |
| echomimic | Apache-2.0 | https://huggingface.co/BadToBest/EchoMimic plus third-party component sources listed in official README. | Do not redistribute EchoMimic checkpoints or dependency weights. | Demo-image provenance note in README means examples should not be reused as benchmark assets without independent permission. |
| hallo2 | MIT_WITH_SLAB_HIGH_RES_CAUTION | https://huggingface.co/fudan-generative-ai/hallo2 plus separately listed source repos for required components. | Do not redistribute Hallo2 pretrained models or third-party component weights. | GitHub shows MIT license, but README states the high-resolution feature is modified from CodeFormer and subject to S-Lab License 1.0. |

Public examples for this benchmark should use only owned, explicitly licensed, synthetic, public-domain, or otherwise written-permission media. The repository license applies only to benchmark harness code and documentation authored here.
