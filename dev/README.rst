==========
bisos.full
==========

.. contents::
   :depth: 3
..

Overview
========

bisos.core: is a top level module that requires core BISOS (ByStar
Internet Services OS) modules.

Main required modules are:

-  unisos.common

-  unisos.ucf

-  unisos.icm

-  unisos.icmExamples

-  bisos.common

-  bisos.bx-bases

-  bisos.bootstrap

-  bisos.examples

-  blee.icmPlayer

bisos.all: is a top level module that requires core BISOS and all BISOS
Pkgs (Feature Areas).

In addition to bisos.core, bisos.all required modules are:

-  bisos.lcnt

-  unisos.x822Msg

-  unisos.marme

-  bisos.things

-  bisos.gossonot

The following suffixes and prefixes are used to indicate purpose.

-  Example – Code/text that illustrates a particular usage

-  Begin – A Template to be used as a beginning point for new code

-  Start – Script that insert “Begin” for new code

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Documentation
=============

Part of ByStar Digital Ecosystem http://www.by-star.net.

This module’s primary documentation is in
http://www.by-star.net/PLPC/180047

Installation
============

::

    sudo pip install bisos.examples

Usage
=====

::

    /usr/local/bin/icmStart.py
    /usr/local/bin/icmExamples.py
