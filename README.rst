=======
ems-cli
=======

.. image:: https://codeclimate.com/github/tomi77/ems-cli/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/ems-cli
   :alt: Code Climate

CLI for EVO Media Server

Commands
========

ems
---

.. sourcecode:: sh

 ems --uri="http://127.0.0.1:7777" add_stream_alias --expire-period=-300 bunny video1

ems-add-group-name-alias
------------------------

Creates secondary name(s) for group name.

.. sourcecode:: sh

 ems-add-group-name-alias --uri="http://127.0.0.1:7777" MyGroup TestGroupAlias

ems-add-stream-alias
--------------------

Create secondary name(s) for internal streams.

.. sourcecode:: sh

 ems-add-stream-alias --uri="http://127.0.0.1:7777" --expire-period=-300 bunny video1

ems-create-dash-stream
----------------------

Create Dynamic Adaptive Streaming over HTTP (DASH) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-dash-stream --uri="http://127.0.0.1:7777" --group-name=dash testpullStream "../evo-webroot"

ems-create-hds-stream
---------------------

Create an HDS (HTTP Dynamic Streaming) stream out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-hds-stream --uri="http://127.0.0.1:7777" --group-name=hds --playlist-type=rolling testpullStream "../evo-webroot"

ems-create-hls-stream
---------------------

Create an HTTP Live Stream (HLS) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-hls-stream --uri="http://127.0.0.1:7777" --bandwidths=128 --group-name=hls --playlist-type=rolling --playlist-length=10 --chunk-length=5 hlstest "/MyWebRoot/"
