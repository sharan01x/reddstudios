var cursor = document.getElementById('cursor');
var timeoutId, moveTimeoutId;

document.addEventListener('mousemove', function (e) {
    var x = e.clientX + Math.random() * 100 - 50; // Add or subtract up to 50px
    var y = e.clientY + Math.random() * 100 - 50; // Add or subtract up to 50px

    // Clear the previous move timeout
    clearTimeout(moveTimeoutId);

    // Set a new move timeout
    moveTimeoutId = setTimeout(function () {
        cursor.style.left = x + 'px';
        cursor.style.top = y + 'px';
        cursor.style.opacity = 0.2; // Make the circle more transparent when in motion
    }, 2000); // Delay in milliseconds before the circle starts moving

    // Clear the previous opacity timeout
    clearTimeout(timeoutId);

    // Set a new opacity timeout
    timeoutId = setTimeout(function () {
        cursor.style.opacity = 0.7; // Restore the original opacity when the mouse stops moving
    }, 1500); // Delay in milliseconds
});

var cursor2 = document.getElementById('cursor2');
var timeoutId2, moveTimeoutId2;

document.addEventListener('mousemove', function (e) {
    var x = e.clientX + Math.random() * 100 - 20; // Add or subtract up to 50px
    var y = e.clientY + Math.random() * 100 - 20; // Add or subtract up to 50px

    // Clear the previous move timeout
    clearTimeout(moveTimeoutId2);

    // Set a new move timeout
    moveTimeoutId2 = setTimeout(function () {
        cursor2.style.left = x + 'px';
        cursor2.style.top = y + 'px';
        cursor2.style.opacity = 0.4; // Make the circle more transparent when in motion
    }, 2500); // Delay in milliseconds before the circle starts moving

    // Clear the previous opacity timeout
    clearTimeout(timeoutId2);

    // Set a new opacity timeout
    timeoutId2 = setTimeout(function () {
        cursor2.style.opacity = 0.5; // Restore the original opacity when the mouse stops moving
    }, 1500); // Delay in milliseconds
});

var cursor3 = document.getElementById('cursor3');
var timeoutId3, moveTimeoutId3;

document.addEventListener('mousemove', function (e) {
    var x = e.clientX + Math.random() * 100 - 30; // Add or subtract up to 50px
    var y = e.clientY + Math.random() * 100 - 30; // Add or subtract up to 50px

    // Clear the previous move timeout
    clearTimeout(moveTimeoutId3);

    // Set a new move timeout
    moveTimeoutId3 = setTimeout(function () {
        cursor3.style.left = x + 'px';
        cursor3.style.top = y + 'px';
        cursor3.style.opacity = 0.4; // Make the circle more transparent when in motion
    }, 1500); // Delay in milliseconds before the circle starts moving

    // Clear the previous opacity timeout
    clearTimeout(timeoutId3);

    // Set a new opacity timeout
    timeoutId3 = setTimeout(function () {
        cursor3.style.opacity = 0.5; // Restore the original opacity when the mouse stops moving
    }, 1500); // Delay in milliseconds
});