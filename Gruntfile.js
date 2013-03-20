

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
  var lessFiles = {
    'src/substanced/substanced/sdi/static/css/sdi_bootstrap.css': [
      'src/substanced/substanced/sdi/static/css/sdi_bootstrap.less'
    ],
    'src/substanced/substanced/sdi/static/css/sdi_slickgrid.css': [
      'src/substanced/substanced/sdi/static/css/sdi_slickgrid.less'
    ]
  };


  // provide a flat listing of source files for watch
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
  for(prop in lessFiles) {
    if (lessFiles.hasOwnProperty(prop)) {
      allFiles = allFiles.concat(lessFiles[prop]);
    }
  }


  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      options: {
        banner: '/*! Built by <%= pkg.name %> */\n'
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
    less: {
      'default': {
        options: {
          paths: ['src/substanced/substanced/sdi/static/css']
        },
        files: lessFiles
      },
      minify: {
        options: {
          paths: ['src/substanced/substanced/sdi/static/css'],
          yuicompress: true
        },
        files: lessFiles
      }
    },
    watch: {
      options: {
        debounceDelay: 250
      },
      'default': {
        files: allFiles,
        tasks: ['concat:js', 'concat:css', 'less:default']
      },
      minify: {
        files: allFiles,
        tasks: ['uglify:js', 'concat:css', 'less:minify']
      }
    }
  });

  // Load the task plugins.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-less');


  // Default task(s).
  grunt.registerTask('default', ['concat:js', 'concat:css', 'less:default']);
  grunt.registerTask('minify', ['uglify:js', 'concat:css', 'less:minify']);

  grunt.registerTask('watch-default', ['watch:default']);
  grunt.registerTask('watch-minify', ['watch:minify']);


};
