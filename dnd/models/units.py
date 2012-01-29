from django.db import models

from dnd.models.abstract import AbstractLibraryModel
from dnd.constants.database import STND_CHAR_LIMIT, STND_ID_CHAR_LIMIT

class ActionTimeDuration(AbstractLibraryModel):
    """
    A length of time in actions.
    """

    time = models.IntegerField(blank=False)

# TODO: Make a measurement module:
#   - mass
#   - time
#   - distance
#   - volume
#   - cost
