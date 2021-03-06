from django.db import models

from dnd.constants.database import STND_CHAR_LIMIT, STND_ID_CHAR_LIMIT
from dnd.models.library_entities.abstract import AbstractDnDEntity
from dnd.models.modifiers.modifiers import Modifier

class Condition(AbstractDnDEntity):
    """
    A condition in which something can be.
    """

    modifiers = models.ManyToManyField(
        Modifier,
        related_name="conditions",
        blank=True)
    short_description = models.CharField(
        max_length=STND_CHAR_LIMIT,
        blank=True)
    #if this condition is a one-off, e.g from a spell (and only from that)
    specific = models.BooleanField(default=False)
    prev = models.ForeignKey(
        "Condition",
        related_name="next",
        blank=True)
