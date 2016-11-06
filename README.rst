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

ems-create-ingest-point
-----------------------

Creates an RTMP ingest point.

.. sourcecode:: sh

 ems-create-ingest-point --uri="http://127.0.0.1:7777" theIngestPoint useMeToViewStream

ems-create-mss-stream
---------------------

Create a Microsoft Smooth Stream (MSS) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-mss-stream --uri="http://127.0.0.1:7777" --group-name=mss testpullStream "../evo-webroot"

ems-flush-group-name-aliases
----------------------------

Invalidates all group name aliases.

.. sourcecode:: sh

 ems-flush-group-name-aliases --uri="http://127.0.0.1:7777"

ems-flush-stream-aliases
------------------------

Invalidates all stream aliases.

.. sourcecode:: sh

 ems-flush-stream-aliases --uri="http://127.0.0.1:7777"

ems-get-config-info
-------------------

Information of the stream by the configId.

.. sourcecode:: sh

 ems-get-config-info --uri="http://127.0.0.1:7777" 1

ems-get-group-name-by-alias
---------------------------

Returns the group name given the alias name.

.. sourcecode:: sh

 ems-get-group-name-by-alias --uri="http://127.0.0.1:7777" TestGroupAlias

ems-get-stream-info-by-id
-------------------------

Detailed set of information about a stream.

.. sourcecode:: sh

 ems-get-stream-info-by-id --uri="http://127.0.0.1:7777" 1

ems-get-stream-info-by-name
---------------------------

Detailed set of information about a stream.

.. sourcecode:: sh

 ems-get-stream-info-by-name --uri="http://127.0.0.1:7777" testpullStream

ems-get-streams-count
---------------------

Number of active streams.

.. sourcecode:: sh

 ems-get-streams-count --uri="http://127.0.0.1:7777"

ems-is-stream-running-by-id
---------------------------

Checks a specific stream if it is running or not.

.. sourcecode:: sh

 ems-is-stream-running-by-id --uri="http://127.0.0.1:7777" 1

ems-is-stream-running-by-name
-----------------------------

Checks a specific stream if it is running or not.

.. sourcecode:: sh

 ems-is-stream-running-by-name --uri="http://127.0.0.1:7777" testStream
