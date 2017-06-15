"""
This package contains implementations of various streaming corpus I/O format.
"""

# bring corpus classes directly into package namespace, to save some typing
from .indexedcorpus import IndexedCorpus  # must appear before the other classes # noqa: F401

from .mmcorpus import MmCorpus  # noqa: F401
from .bleicorpus import BleiCorpus  # noqa: F401
from .svmlightcorpus import SvmLightCorpus  # noqa: F401
from .lowcorpus import LowCorpus  # noqa: F401
from .dictionary import Dictionary  # noqa: F401
from .hashdictionary import HashDictionary  # noqa: F401
from .wikicorpus import WikiCorpus  # noqa: F401
from .textcorpus import TextCorpus  # noqa: F401
from .ucicorpus import UciCorpus  # noqa: F401
from .malletcorpus import MalletCorpus  # noqa: F401
