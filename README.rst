=======
ems-cli
=======

.. image:: https://codeclimate.com/github/tomi77/ems-cli/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/ems-cli
   :alt: Code Climate

CLI for EVO Media Server

Commands
========

ems-add-group-name-alias
------------------------

Creates secondary name(s) for group name.

.. sourcecode:: sh

 ems-add-group-name-alias --connection-uri="http://127.0.0.1:7777" MyGroup TestGroupAlias

ems-add-stream-alias
--------------------

Create secondary name(s) for internal streams.

.. sourcecode:: sh

 ems-add-stream-alias --connection-uri="http://127.0.0.1:7777" --expire-period=-300 bunny video1

ems-create-dash-stream
----------------------

Create Dynamic Adaptive Streaming over HTTP (DASH) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-dash-stream --connection-uri="http://127.0.0.1:7777" --group-name=dash testpullStream "../evo-webroot"

ems-create-hds-stream
---------------------

Create an HDS (HTTP Dynamic Streaming) stream out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-hds-stream --connection-uri="http://127.0.0.1:7777" --group-name=hds --playlist-type=rolling testpullStream "../evo-webroot"

ems-create-hls-stream
---------------------

Create an HTTP Live Stream (HLS) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-hls-stream --connection-uri="http://127.0.0.1:7777" --bandwidths=128 --group-name=hls --playlist-type=rolling --playlist-length=10 --chunk-length=5 hlstest "/MyWebRoot/"

ems-create-ingest-point
-----------------------

Creates an RTMP ingest point.

.. sourcecode:: sh

 ems-create-ingest-point --connection-uri="http://127.0.0.1:7777" theIngestPoint useMeToViewStream

ems-create-mss-stream
---------------------

Create a Microsoft Smooth Stream (MSS) out of an existing H.264/AAC stream.

.. sourcecode:: sh

 ems-create-mss-stream --connection-uri="http://127.0.0.1:7777" --group-name=mss testpullStream "../evo-webroot"

ems-flush-group-name-aliases
----------------------------

Invalidates all group name aliases.

.. sourcecode:: sh

 ems-flush-group-name-aliases --connection-uri="http://127.0.0.1:7777"

ems-flush-stream-aliases
------------------------

Invalidates all stream aliases.

.. sourcecode:: sh

 ems-flush-stream-aliases --connection-uri="http://127.0.0.1:7777"

ems-get-config-info
-------------------

Information of the stream by the configId.

.. sourcecode:: sh

 ems-get-config-info --connection-uri="http://127.0.0.1:7777" 1

ems-get-group-name-by-alias
---------------------------

Returns the group name given the alias name.

.. sourcecode:: sh

 ems-get-group-name-by-alias --connection-uri="http://127.0.0.1:7777" TestGroupAlias

ems-get-stream-info-by-id
-------------------------

Detailed set of information about a stream.

.. sourcecode:: sh

 ems-get-stream-info-by-id --connection-uri="http://127.0.0.1:7777" 1

ems-get-stream-info-by-name
---------------------------

Detailed set of information about a stream.

.. sourcecode:: sh

 ems-get-stream-info-by-name --connection-uri="http://127.0.0.1:7777" testpullStream

ems-get-streams-count
---------------------

Number of active streams.

.. sourcecode:: sh

 ems-get-streams-count --connection-uri="http://127.0.0.1:7777"

ems-is-stream-running-by-id
---------------------------

Checks a specific stream if it is running or not.

.. sourcecode:: sh

 ems-is-stream-running-by-id --connection-uri="http://127.0.0.1:7777" 1

ems-is-stream-running-by-name
-----------------------------

Checks a specific stream if it is running or not.

.. sourcecode:: sh

 ems-is-stream-running-by-name --connection-uri="http://127.0.0.1:7777" testStream

ems-list-config
---------------

List with all push/pull configurations.

.. sourcecode:: sh

 ems-list-config --connection-uri="http://127.0.0.1:7777"

ems-list-group-name-aliases
---------------------------

A complete list of group name aliases.

.. sourcecode:: sh

 ems-list-group-name-aliases --connection-uri="http://127.0.0.1:7777"

ems-list-http-streaming-sessions
--------------------------------

All currently active HTTP streaming sessions.

.. sourcecode:: sh

 ems-list-http-streaming-sessions --connection-uri="http://127.0.0.1:7777"

ems-list-ingest-points
----------------------

The currently available Ingest Points.

.. sourcecode:: sh

 ems-list-ingest-points --connection-uri="http://127.0.0.1:7777"

ems-list-stream-aliases
-----------------------

A complete list of aliases.

.. sourcecode:: sh

 ems-list-stream-aliases --connection-uri="http://127.0.0.1:7777"

ems-list-streams
----------------

.. sourcecode:: sh

 ems-list-streams --connection-uri="http://127.0.0.1:7777"

ems-list-streams-ids
--------------------

A list of IDs for every active stream.

.. sourcecode:: sh

 ems-list-streams-ids --connection-uri="http://127.0.0.1:7777"

ems-pull-stream
---------------

Pull in a stream from an external source.

.. sourcecode:: sh

 ems-pull-stream --connection-uri="http://127.0.0.1:7777" --local-stream-name=testpullStream "rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4"

ems-push-stream
---------------

Push a local stream to an external destination.

.. sourcecode:: sh

 ems-push-stream --connection-uri="http://127.0.0.1:7777" --local-stream-name=testpullstream --target-stream-name=testpushStream "rtmp://DestinationAddress/live"

ems-record
----------

Records any inbound stream.

.. sourcecode:: sh

 ems-record --connection-uri="http://127.0.0.1:7777" --type=mp4 --overwrite=1 testpullstream "../media/testRecord"

ems-remove-config-by-id
-----------------------

Stop the stream and remove the corresponding configuration entry.

.. sourcecode:: sh

 ems-remove-config-by-id --connection-uri="http://127.0.0.1:7777" 55

ems-remove-config-by-group-name
-------------------------------

Stop the stream and remove the corresponding configuration entry.

.. sourcecode:: sh

 ems-remove-config-by-group-name --connection-uri="http://127.0.0.1:7777" hls

ems-remove-group-name-alias
---------------------------

Remove an alias of a group.

.. sourcecode:: sh

 ems-remove-group-name-alias --connection-uri="http://127.0.0.1:7777" TestGroupAlias

ems-remove-ingest-point
-----------------------

Remove an RTMP ingest point.

.. sourcecode:: sh

 ems-remove-ingest-point --connection-uri="http://127.0.0.1:7777" theIngestPoint

ems-remove-stream-alias
-----------------------

Remove an alias of a stream.

.. sourcecode:: sh

 ems-remove-stream-alias --connection-uri="http://127.0.0.1:7777" video1

ems-shutdown-stream-by-id
-------------------------

Terminate a stream.

.. sourcecode:: sh

 ems-shutdown-stream-by-id --connection-uri="http://127.0.0.1:7777" 55

ems-shutdown-stream-by-name
---------------------------

Terminate a stream.

.. sourcecode:: sh

 ems-shutdown-stream-by-name --connection-uri="http://127.0.0.1:7777" testpullstream

ems-transcode
-------------

Change the compression characteristics of an audio/video stream.

.. sourcecode:: sh

 ems-transcode --connection-uri="http://127.0.0.1:7777" --group_name=group --video-bitrates=200k "rtmp://s2pchzxmtymn2k.cloudfront.net/cfx/st/mp4:sintel.mp4" stream1
