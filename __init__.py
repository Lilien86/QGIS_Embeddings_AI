"""QGIS Embeddings AI - Unlock geospatial foundation models in QGIS."""

from .embeddings_plugin import EmbeddingsAI


def classFactory(iface):
    """Load QGIS Embeddings AI plugin class."""
    return EmbeddingsAI(iface)
