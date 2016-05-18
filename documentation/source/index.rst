.. _index:

defcon
======

defcon is a set of UFO based objects optimized for use in font editing applications. The objects are built to be lightweight, fast and flexible. The objects are very bare-bones and they are not meant to be end-all, be-all objects. Rather, they are meant to provide :ref:`base functionality <Subclassing>` so that you can focus on your application's behavior, not :ref:`object observing <Notifications>` or :ref:`maintaining cached data <Representations>`.

Basic Usage
^^^^^^^^^^^

defcon is very easy to use::

  from defcon import Font
  font = Font()
  # now do some stuff!


Concepts
^^^^^^^^

.. toctree::
   :maxdepth: 1

   concepts/notifications
   concepts/subclassing
   concepts/externalchanges
   concepts/representations


Objects
^^^^^^^

.. toctree::
   :maxdepth: 1

   objects/font
   objects/layer
   objects/glyph
   objects/contour
   objects/component
   objects/point
   objects/anchor
   objects/info
   objects/kerning
   objects/groups
   objects/features
   objects/lib
   objects/unicodedata
   objects/notificationcenter
   objects/base
   objects/layerSet


Dependencies
^^^^^^^^^^^^

* `FontTools <https://github.com/behdad/fonttools>`_
* `RoboFab <http://robofab.com>`_
* `ufoLib <https://github.com/unified-font-object/ufoLib>`_


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

