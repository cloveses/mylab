from creature import Creature
from item import Item
from location import Location

def process_locations(source):
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<PATHS>` (page 3 of the assignment description).

    TODO: Read the given configuration file and return a list of Location
    objects based on the file's contents.
    """

def process_items(source, locations):
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<ITEMS>` (page 4 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and return a list of Item objects
    based on the file's contents. You might also want to link the new Item
    objects to their starting Locations.
    """

def process_creatures(source, locations):
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<CHASERS>` (page 5 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and return a list of Creature
    objects based on the file's contents. You might also wan to find a way to
    link each Goosechaser with their starting locations.
    """

def process_exits(source, locations):
    """
    Parameters:
    - `source`: The (path to) a configuration file as described under the
                heading `<EXITS>` (page 5 of the assignment description.)
    - `locations`: A list of Location objects.

    TODO: Read the given configuration file and use this to indicate which
    Location objects allow the use of the FLEE command.
    """
