

module.exports = function(grunt) {

    var jsFiles = {
        'src/substanced/substanced/sdi/static/js/slickgrid.upstream.js': [
            'src/slickgrid/plugins/slick.responsiveness.js',
            'src/slickgrid/bootstrap/bootstrap-slickgrid.js',
            'src/slickgrid/lib/jquery-ui-1.8.16/jquery.ui.core.js',
            'src/slickgrid/lib/jquery-ui-1.8.16/jquery.ui.widget.js',
            'src/slickgrid/lib/jquery-ui-1.8.16/jquery.ui.mouse.js',
            'src/slickgrid/lib/jquery-ui-1.8.16/jquery.ui.resizable.js',
            'src/slickgrid/lib/jquery-ui-1.8.16/jquery.ui.sortable.js',
            'src/slickgrid/lib/jquery.event.drag-2.0.min.js',
            'src/slickgrid/lib/jquery.event.drop-2.0.min.js',
            'src/slickgrid/slick.dataview.js',
            'src/slickgrid/slick.core.js',
            'src/slickgrid/slick.grid.js',
            'src/slickgrid/plugins/slick.rowselectionmodel.js',
            'src/slickgrid/plugins/slick.checkboxselectcolumn.js',
            'src/slickgrid/plugins/slick.responsiveness.js',
            'src/slickgrid/bootstrap/bootstrap-slickgrid.js'
        ]
    };
    var cssFiles = {
        'src/substanced/substanced/sdi/static/css/slick.grid.upstream.css': [
            'src/slickgrid/slick.grid.css',
            'src/slickgrid/controls/slick.columnpicker.css'
        ]
    };
    // This is silly, but watch requires a flat array format, which we cannot
    // provide via a template expression.
    var allFiles = [];
    for(var prop in jsFiles) {
        if (jsFiles.hasOwnProperty(prop)) {
            allFiles = allFiles.concat(jsFiles[prop]);
        }
    } 
    for(prop in cssFiles) {
        if (cssFiles.hasOwnProperty(prop)) {
            allFiles = allFiles.concat(cssFiles[prop]);
        }
    }
    
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            options: {
                banner: '/*! <%= pkg.name %> */\n'
            },
            js: {
                files: jsFiles
            },
            css: {
                files: cssFiles
            }
        },
        uglify: {
            options: {
                banner: '<%= concat.options.banner %>'
            },
            js: {
                files: jsFiles
            }
        },
        watch: {
            options: {
                debounceDelay: 250
            },
            'default': {
                files: allFiles,
                tasks: ['concat']
            },
            'minify': {
                files: allFiles,
                tasks: ['uglify', 'concat:css']
            }
        }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', ['concat']);
    grunt.registerTask('minify', ['concat:css', 'uglify']);

    grunt.registerTask('watch-default', ['watch:default']);
    grunt.registerTask('watch-minify', ['watch:minify']);

};
