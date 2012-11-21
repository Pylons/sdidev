#! /bin/sh

# This should be .... python, to allow it to run in windows.
# ... properly integrated as a console script or in supervisor
# ... actually minify (uglify) and not just concat
# ... should autocompile anyway, if there are changes.
#
# For now, just run this to update the javascripts in substanced.

HERE=`dirname $0`
SLICKGRID=$HERE/../src/slickgrid
SUBSTANCED=$HERE/../src/substanced/substanced/sdi/static/js

cat \
    $SLICKGRID/lib/jquery-ui-1.8.16.custom.min.js \
    $SLICKGRID/lib/jquery.event.drag-2.0.min.js \
    $SLICKGRID/lib/jquery.event.drop-2.0.min.js \
    $SLICKGRID/slick.dataview.js \
    $SLICKGRID/slick.core.js \
    $SLICKGRID/slick.grid.js \
    $SLICKGRID/bootstrap/bootstrap-slickgrid.js \
    $SUBSTANCED/slickgrid-config.js \
    > $SUBSTANCED/slickgrid.min.js


    #$SLICKGRID/slick.editors.js \
    #$SLICKGRID/plugins/slick.rowselectionmodel.js \
    #$SLICKGRID/controls/slick.columnpicker.js \

