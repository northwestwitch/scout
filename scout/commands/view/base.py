import logging

import click

from .panels import panels
from .users import users
from .institutes import institutes
from .diseases import diseases
from .hpo import hpo
from .whitelist import whitelist
from .aliases import aliases
from .individuals import individuals
from .index import index
from .intervals import intervals
from .collections import collections
from .transcripts import transcripts
from .case import cases


LOG = logging.getLogger(__name__)


@click.group()
def view():
    """
    View objects from the database. This command is used to get a overview of objects in the
    database. To get serialisable things use `scout export`
    """
    pass


view.add_command(panels) # done!
view.add_command(users) # done!
view.add_command(institutes) # done!
view.add_command(diseases) # done!
view.add_command(hpo) # done!
view.add_command(whitelist) # done!
view.add_command(aliases) # done!
view.add_command(individuals) # done!
view.add_command(index)
view.add_command(intervals)
view.add_command(collections)
view.add_command(transcripts)
view.add_command(cases)
