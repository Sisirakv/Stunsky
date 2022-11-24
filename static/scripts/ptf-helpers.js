/***********************************************
 * Helpers
 ***********************************************/

'use strict';

/**
 * Initialize main helper object
 */
var PTFJS = {
	window: jQuery(window),
	document: jQuery(document),
	html: jQuery('html'),
	body: jQuery('body'),
	is_safari: /^((?!chrome|android).)*safari/i.test(navigator.userAgent),
	is_firefox: navigator.userAgent.toLowerCase().indexOf('firefox') > -1,
	is_chrome: /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor),
	is_ie10: navigator.appVersion.indexOf('MSIE 10') !== -1,
	transitionEnd: 'transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd',
	animIteration: 'animationiteration webkitAnimationIteration oAnimationIteration MSAnimationIteration',
	animationEnd: 'animationend webkitAnimationEnd',
	getMousePos: function (e) {
		var posx = 0;
		var posy = 0;
		if (!e) e = window.event;
		if (e.pageX || e.pageY) {
			posx = e.pageX;
			posy = e.pageY;
		} else if (e.clientX || e.clientY) {
			posx = e.clientX + PTFJS.body.scrollLeft() + PTFJS.document.scrollLeft();
			posy = e.clientY + PTFJS.body.scrollTop() + PTFJS.document.scrollTop();
		}
		return {
			x: posx,
			y: posy
		}
	}
};

/**
 * Detects whether user is viewing site from a mobile device
 */
PTFJS.isMobile = {
	Android: function () {
		return navigator.userAgent.match(/Android/i);
	},
	BlackBerry: function () {
		return navigator.userAgent.match(/BlackBerry/i);
	},
	iOS: function () {
		return navigator.userAgent.match(/iPhone|iPad|iPod/i);
	},
	Opera: function () {
		return navigator.userAgent.match(/Opera Mini/i);
	},
	Windows: function () {
		return navigator.userAgent.match(/IEMobile/i);
	},
	any: function () {
		return (PTFJS.isMobile.Android() || PTFJS.isMobile.BlackBerry() || PTFJS.isMobile.iOS() || PTFJS.isMobile.Opera() || PTFJS.isMobile.Windows());
	}
};

/**
 * Debounce resize
 */
var resizeArr = [];
var resizeTimeout;
PTFJS.window.on('load resize orientationchange', function(e) {
	if (resizeArr.length) {
		clearTimeout(resizeTimeout);
		resizeTimeout = setTimeout(function() {
			for (var i = 0; i < resizeArr.length; i++) {
				resizeArr[i](e);
			}
		}, 250);
	}
});

PTFJS.debounceResize = function(callback) {
	if (typeof callback === 'function') {
		resizeArr.push(callback);
	} else {
		window.dispatchEvent(new Event('resize'));
	}
}

/**
 * Throttle scroll
 */
var throttleArr = [];
var didScroll;
var delta = 5;
var lastScrollTop = 0;

PTFJS.window.on('load resize scroll orientationchange', function() {
	if (throttleArr.length) {
		didScroll = true;
	}
});

function hasScrolled() {

	var scrollTop = PTFJS.window.scrollTop(),
		windowHeight = PTFJS.window.height(),
		documentHeight = PTFJS.document.height(),
		scrollState = '';

	// Make sure they scroll more than delta
	if (Math.abs(lastScrollTop - scrollTop) <= delta) {
		return;
	}

	if (scrollTop > lastScrollTop) {
		scrollState = 'down';
	} else if (scrollTop < lastScrollTop) {
		scrollState = 'up';
	} else {
		scrollState = 'none';
	}

	if (scrollTop === 0) {
		scrollState = 'start';
	} else if (scrollTop >= documentHeight - windowHeight) {
		scrollState = 'end';
	}

	for (var i in throttleArr) {
		if (typeof throttleArr[i] === 'function') {
			throttleArr[i](scrollState, scrollTop, lastScrollTop, PTFJS.window);
		}
	}

	lastScrollTop = scrollTop;
}

setInterval(function() {
	if (didScroll) {
		didScroll = false;
		window.requestAnimationFrame(hasScrolled);
	}
}, 250);

PTFJS.throttleScroll = function(callback) {
	if (typeof callback === 'function') {
		throttleArr.push(callback);
	}
}


$(document).on('submit', 'form.ajax', function (e) {
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var reset = $this.hasClass('reset');
    var reload = $this.hasClass('reload');
    var redirect = $this.hasClass('redirect');
    var redirect_url = $this.attr('data-redirect');

    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function (data) {

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;

            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                Swal.fire({
                    title: title,
                    html: message,
                    icon: 'success',
                }).then(function () {
                    if (redirect) {
                        window.location.href = redirect_url;
                    }
                    if (reload) {
                        window.location.reload();
                    }
                    if (reset) {
                        window.location.reset();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    html: message,
                    icon: "error"
                });

            }
        },
        error: function (data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                html: message,
                icon: "error"
            });
        }
    });
});