var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;

gulp.task('sass', function () {
    return gulp.src('../core/static/scss/app.scss')
        .pipe(concat('style.css'))
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('../core/static/css'));
});

gulp.task('runserver', function() {
    var proc = exec('python3 ../manage.py runserver')
});

gulp.task('browserSync', ['runserver'], function() {
    browserSync.init({
        notify: false,
        port: 8000,
        proxy: 'localhost:8000'
    })
});

gulp.task('watch', ['browserSync', 'sass'], function() {
    gulp.watch('../core/static/scss/**/*.scss', ['sass']);
    gulp.watch('../core/static/js/**/*.js', browserSync.reload);
});
