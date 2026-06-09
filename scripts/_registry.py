"""Small registry helpers for the initial YAML shape.

The project intentionally avoids PyYAML in the skeleton. This parser supports
the simple candidates.yaml structure used here and should be replaced with a
real YAML parser if the registry becomes more complex.
"""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_candidates(registry_path: str | Path = "candidates/candidates.yaml") -> list[dict[str, object]]:
    path = Path(registry_path)
    if not path.is_absolute():
        path = repo_root() / path
    if not path.exists():
        raise FileNotFoundError(f"registry not found: {path}")

    candidates: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    active_list_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.strip()
        if stripped == "candidates:":
            continue
        if stripped.startswith("- "):
            item = stripped[2:]
            if ":" in item:
                key, value = item.split(":", 1)
                current = {key.strip(): _parse_scalar(value)}
                candidates.append(current)
                active_list_key = None
            elif current is not None and active_list_key:
                current.setdefault(active_list_key, [])
                current[active_list_key].append(_parse_scalar(item))  # type: ignore[index, union-attr]
            continue
        if current is None or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            current[key] = _parse_scalar(value)
            active_list_key = None
        else:
            current[key] = []
            active_list_key = key

    return candidates


def find_candidate(candidate_id: str, registry_path: str | Path = "candidates/candidates.yaml") -> dict[str, object] | None:
    for candidate in load_candidates(registry_path):
        if candidate.get("id") == candidate_id:
            return candidate
    return None
