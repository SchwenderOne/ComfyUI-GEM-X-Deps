"""
ComfyUI-GEM-X-Deps — a no-op "deps carrier" pack (registers ZERO nodes).

Its only job: ship GEM-X's requirements.txt so ComfyUI Manager pip-installs them when
this repo is added via *Install via Git URL*. A manually-uploaded ComfyUI-GEM-X folder
does NOT auto-pip its requirements (only Manager Git-URL installs do), so install this
FIRST, then the real ComfyUI-GEM-X pack imports cleanly.
See docs/ERROR_PATTERNS.md D1.
"""
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
