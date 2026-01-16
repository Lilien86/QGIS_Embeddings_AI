# QGIS Embeddings AI

A QGIS plugin that unlocks the power of geospatial foundation models for advanced spatial analysis.

![Plugin Version](https://img.shields.io/badge/version-0.1.0-blue)
![QGIS](https://img.shields.io/badge/QGIS-3.28%2B-green)
![License](https://img.shields.io/badge/license-GPL--3.0-lightgrey)

## What are Geospatial Foundation Models?

Foundation models are large-scale AI systems pre-trained on massive amounts of diverse geospatial data. They learn universal representations of Earth's surface that can be adapted to countless downstream tasks.

### How they work

**Training**: Models are trained on petabyte-scale datasets combining satellite imagery (optical + radar), elevation data, climate variables, and text from Wikipedia and biodiversity databases.

**Embeddings**: The model converts each location into a 64-dimensional vector (an "embedding"), a compact mathematical fingerprint encoding land cover patterns, seasonal dynamics, spatial context, and semantic meaning.

**Applications**: These embeddings enable similarity search, zero-shot classification, multi-modal fusion, and text-to-map queries.

### Why embeddings?

Embeddings provide 16x data compression while preserving information, enable instant analysis through pre-computed representations, support one model for many tasks, and work anywhere on Earth across sensors and time periods.

## Supported Foundation Models

**AlphaEarth** (Google DeepMind): General-purpose Earth observation foundation model trained on petabyte-scale geospatial data.

## Features

Point-based similarity search with configurable search radius (0.5 to 100 km), year selection (2017-2023), visual similarity heatmaps (green = similar, red = different), and Google Satellite basemap integration.

## Requirements

**QGIS 3.28+**

**Google Earth Engine Plugin** installed from QGIS Plugin Manager

**Google Cloud Project** with Earth Engine API enabled

**GEE Authentication** connected and authenticated

## Installation

### From QGIS Plugin Manager

Open QGIS, go to Plugins > Manage and Install Plugins, search for "QGIS Embeddings AI", and click Install.

### Manual Installation

Download or clone this repository, copy the folder to your QGIS plugins directory (macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`, Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`, Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`), restart QGIS, and enable in Plugins > Manage and Install Plugins.

## Usage

Click the QGIS Embeddings AI icon in the toolbar. Optionally import a basemap for reference. Click "Add Point" to select a reference location on the map. Configure search parameters (year for satellite data 2017-2023, buffer radius in kilometers, threshold for maximum dissimilarity 0-1, resolution in meters). Click "Search Similarity" and wait for results. A new raster layer shows similarity where green indicates high similarity, yellow medium, and red low similarity.

## Technical Details

### AlphaEarth Architecture

Vision Transformer with STP (Space-Time-Precision) blocks processing 10m resolution imagery from Sentinel-2, Landsat, SAR, DEM, ERA5, and text sources. Outputs 64-dimensional unit vectors on a hypersphere using von Mises-Fisher distribution. Trained via self-supervised contrastive learning on petabyte-scale data. Similarity measured by Euclidean distance in embedding space.

### Data Flow

User selects point, extract mean embedding vector, calculate distance for search area, visualize as heatmap.

## Author

**Lilien Auger**  
[LinkedIn](https://www.linkedin.com/in/lilien-auger/)

## License

GPL-3.0 License. See LICENSE file for details.

## Acknowledgments

Google DeepMind for AlphaEarth, Google Earth Engine team, and the QGIS community.
