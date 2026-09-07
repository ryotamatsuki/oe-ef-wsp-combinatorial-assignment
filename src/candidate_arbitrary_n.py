"""Backward-compatible import for the frozen arbitrary-n mechanism.

The theorem-status implementation now lives in `src.mechanism_arbitrary_n`.
"""
from .mechanism_arbitrary_n import group_allocation

__all__ = ["group_allocation"]
