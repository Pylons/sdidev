
var UglifyJS = require("uglify-js");
var fs  = require("fs");

// Check to see if we have the correct number of arguments
var args = process.argv.slice(2);

if (! args[0] || args.length > 2 || 
    args.length == 2 && args[1] != '-m' && args[1] != '--minify') {
    console.log("There is one mandatory parameter, and one option.");
    console.log("\tExample:");
    console.log("\tnode jswatcher.js BUILDOUT_ROOT");
    console.log("\tnode jswatcher.js BUILDOUT_ROOT --minify");
    process.exit(1);
}

// By default, we just concat.
var minify = (args[1] == '-m' || args[1] == '--minify');

function processFiles(files, resultfile, minify) {
    if (minify) {
        result = UglifyJS.minify(files);
        fs.writeFileSync(resultfile, result.code, 'utf8');
    } else {
        fs.writeFileSync(resultfile, 'utf8');
        for (var i=0; i < files.length; i++) {
            var txt = fs.readFileSync(files[i], 'utf8');
            fs.appendFileSync(resultfile, txt, 'utf8');
        }
    }
}

var root = args[0];
var slickgrid = root + '/src/slickgrid';
var substanced = root + '/src/substanced/substanced/sdi/static';

var files = [
    slickgrid + '/plugins/slick.responsiveness.js',
    slickgrid + '/bootstrap/bootstrap-slickgrid.js',
    slickgrid + '/lib/jquery-ui-1.8.16/jquery.ui.core.js',
    slickgrid + '/lib/jquery-ui-1.8.16/jquery.ui.widget.js',
    slickgrid + '/lib/jquery-ui-1.8.16/jquery.ui.mouse.js',
    slickgrid + '/lib/jquery-ui-1.8.16/jquery.ui.resizable.js',
    slickgrid + '/lib/jquery-ui-1.8.16/jquery.ui.sortable.js',
    slickgrid + '/lib/jquery.event.drag-2.0.min.js',
    slickgrid + '/lib/jquery.event.drop-2.0.min.js',
    slickgrid + '/slick.dataview.js',
    slickgrid + '/slick.core.js',
    slickgrid + '/slick.grid.js',
    slickgrid + '/plugins/slick.rowselectionmodel.js',
    slickgrid + '/plugins/slick.checkboxselectcolumn.js',
    slickgrid + '/plugins/slick.responsiveness.js',
    slickgrid + '/bootstrap/bootstrap-slickgrid.js'
];
resultfile = substanced + '/js/slickgrid.upstream.js';
processFiles(files, resultfile, minify);

// css only works with minify = false.
files = [
    slickgrid + '/slick.grid.css',
    slickgrid + '/controls/slick.columnpicker.css'
];
resultfile = substanced + '/css/slick.grid.upstream.css';
processFiles(files, resultfile, false);

console.log('building resources OK');