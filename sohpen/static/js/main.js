(function ($) {
	"use strict";
	
	//meanmenu
	if($.fn.meanmenu){
		$('.mobile-menu').meanmenu({
			meanScreenWidth: 767
		});
	}
	
	//countdown
	

	//owl carousel
	if($.fn.owlCarousel) {
		//banner slider
		$(".banner-slider").owlCarousel({
			items: 1,
			dots: false,
			animateOut: 'slideOutDown',
			animateIn: 'zoomIn',
			autoplay: false,
			loop: true,
			autoplaySpeed: true,
			smartSpeed: 250
		});
		//hm2-speaker-slider
		$(".speaker-slider-hm2").owlCarousel({
			items: 4,
			margin: 30,
			nav: true,
			navText: [
			  "<i class='icofont icofont-thin-left '></i>",
			  "<i class='icofont icofont-thin-right '></i>"
			  ],
			responsive: {
                300: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 4
                },
                1024: {
                    items: 4
                }
            }
		});
		//hm2-speaker-slider
		$(".up-event-slider").owlCarousel({
			items: 3,
			margin: 30,
			nav: true,
			navText: [
			  "<i class='icofont icofont-thin-left '></i>",
			  "<i class='icofont icofont-thin-right '></i>"
			  ],
			responsive: {
                300: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 3
                },
                1024: {
                    items: 3
                }
            }
		});
		
		//team img
		var team_slid = $('.speaker-slider');
		team_slid.owlCarousel({
			items: 1,
			loop: true,
			animateIn: 'fadeInLeft',
			animateOut: 'fadeOutRight',
			nav: true,
			navText: [
			  "<i class='icofont icofont-thin-left '></i>",
			  "<i class='icofont icofont-thin-right '></i>"
			]
		});
		
		//hm2-testm-slider
		$(".testimonial-slider").owlCarousel({
			items: 1,
			margin: 30,
			nav: true,
			navText: [
			  "<i class='icofont icofont-thin-left '></i>",
			  "<i class='icofont icofont-thin-right '></i>"
			  ]
		});
		
		//team content
		var team_slid2 = $('.speaker-info-slider');
		team_slid2.owlCarousel({
			items: 1,
			animateIn: 'fadeInDown',
			animateOut: 'fadeOutDown',
			loop: true
		});
	}
	
	//home1 speaker double slider 
	team_slid.on('translate.owl.carousel', function (property) {
		$('.team-content .owl-dot:eq(' + property.page.index + ')').click();
	});
	team_slid2.on('translate.owl.carousel', function (property) {
		$('.speaker-slider-container .owl-dot:eq(' + property.page.index + ')').click();
	});

	//Popup
	$('.popup-youtube').magnificPopup({
		type: 'iframe'
	});

	$('.image-popup').magnificPopup({
		type: 'image',
		closeOnContentClick: true,
		mainClass: 'mfp-img-mobile',
		image: {
			verticalFit: true
		}

	});

	//sponsor page mixitup
	$('#sponsor-sorting').mixItUp({
		animation: {
             perspectiveDistance: '1000px'
         }
	});
	
	//Initialize wow
	new WOW().init();
	
	//google map
	var googleMapSelector = $('#contactgoogleMap'),
		myCenter = new google.maps.LatLng(27.72834042497272,85.32356565346346);

	function initialize() {
		var mapProp = {
			center: myCenter,
			zoom: 4,
			scrollwheel: false,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			styles:

			[
			{
				"featureType": "administrative",
				"elementType": "all",
				"stylers": [
					{
						"saturation": "-100"
					}
				]
			},
			{
				"featureType": "administrative.province",
				"elementType": "all",
				"stylers": [
					{
						"visibility": "off"
					}
				]
			},
			{
				"featureType": "landscape",
				"elementType": "all",
				"stylers": [
					{
						"saturation": -100
					},
					{
						"lightness": 65
					},
					{
						"visibility": "on"
					}
				]
			},
			{
				"featureType": "poi",
				"elementType": "all",
				"stylers": [
					{
						"saturation": -100
					},
					{
						"lightness": "50"
					},
					{
						"visibility": "simplified"
					}
				]
			},
			{
				"featureType": "road",
				"elementType": "all",
				"stylers": [
					{
						"saturation": "-100"
					}
				]
			},
			{
				"featureType": "road.highway",
				"elementType": "all",
				"stylers": [
					{
						"visibility": "simplified"
					},
				]
			},
			{
				"featureType": "road.arterial",
				"elementType": "all",
				"stylers": [
					{
						"lightness": "30"
					},
				]
			},
			{
				"featureType": "road.local",
				"elementType": "all",
				"stylers": [
					{
						"lightness": "40"
					}
				]
			},
			{
				"featureType": "transit",
				"elementType": "all",
				"stylers": [
					{
						"color": "#000"
					},
					{
						"visibility": "simplified"
					}
				]
			},
			{
				"featureType": "water",
				"elementType": "geometry",
				"stylers": [
					{
						"visibility": "on"
					},

					{
						"color": "#edf0f5"
					}
				]
			},
			{
				"featureType": "water",
				"elementType": "labels",
				"stylers": [
					{
						"color": "#343434"
					}
				]
			}
		]


		};
		var map = new google.maps.Map(document.getElementById("contactgoogleMap"), mapProp);
		var marker = new google.maps.Marker({
			position: myCenter,
			animation: google.maps.Animation.BOUNCE,
			icon: 'img/map-marker.png'
		});
		marker.setMap(map);
	}
	if (googleMapSelector.length) {
		google.maps.event.addDomListener(window, 'load', initialize);
	}
	
	//window load function
	$(window).on('load',function () {
		// Hide preloader slowly 
        $("#preloader").delay(1000).fadeOut("slow");
	});

})(jQuery);