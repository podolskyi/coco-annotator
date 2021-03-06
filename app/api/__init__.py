from flask import Blueprint
from flask_restplus import Api

from .annotations import api as ns_annotations
from .categories import api as ns_categories
from .annotator import api as ns_annotator
from .datasets import api as ns_datasets
from .images import api as ns_images
from .undo import api as ns_undo
from .info import api as ns_info

from ..config import Config

# Create /api/ space
blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title=Config.NAME,
    version=Config.VERSION,
)

# Remove default namespace
api.namespaces.pop(0)

# Setup API namespaces
api.add_namespace(ns_info)
api.add_namespace(ns_images)
api.add_namespace(ns_annotations)
api.add_namespace(ns_categories)
api.add_namespace(ns_annotator)
api.add_namespace(ns_datasets)
api.add_namespace(ns_undo)

