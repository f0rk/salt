'''
Does Nothing
============

The noop state module does nothing. This state is useful for collecting many
resources together via require and then using just this state as a require
elsewhere.

Available Functions
-------------------

The noop state only has a single function, the ``noop`` function

noop
    Do nothing.

    A simple example:

    .. code-block:: yaml

        collection_of_files:
          noop.noop:
            - require:
              - file: foo
              - file: bar
              - pkg: baz

        some-package:
          pkg.installed:
            - require:
              - noop: collection_of_files

'''


def noop(name):
    '''
    Do nothing.

    name
        The name of the noop.

    '''
    return {'name': name,
            'changes': {},
            'result': True,
            'comment': ''}


