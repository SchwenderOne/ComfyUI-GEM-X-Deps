# ComfyUI-GEM-X-Deps

A **no-op** ComfyUI pack (registers no nodes). It exists only to carry the
`requirements.txt` for **ComfyUI-GEM-X** so ComfyUI Manager pip-installs those deps
when added via **Install via Git URL**.

## Why
A node pack placed manually under `custom_nodes/` does **not** get its
`requirements.txt` auto-installed — only Manager-driven Git installs do. So the real
pack import-fails on missing deps (lightning, hydra, py-soma-x, onnxruntime-gpu, …).
Installing this Deps repo via Git URL runs the pip step; then `ComfyUI-GEM-X` loads.

## Use
ComfyUI Manager → *Install via Git URL* → paste this repo's URL → **Restart**.
Then install the real `ComfyUI-GEM-X` pack. Do not let anything change torch
(image pins `2.4.1+cu124`). Keep `requirements.txt` in sync with the real pack.

> Note: GEM-X also needs its vendored `gemx_src/` installed editable; that is handled
> by `ComfyUI-GEM-X/__init__.py` at import time, not by this Deps repo.
