/* ==================================================================================== */
/* Before|After • Comparison Feature v1.5.1 — © Édouard Puginier — https://tazintosh.com */
/* Under Creative Common license Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)     */
/* ==================================================================================== */

function setupComparison(comparisonArea, reset){
	// jQuery(function($){

		/* ========================= Defaults */
		var showHandle = true, // false
			handleSize = 30, // Diameter in px
			showSlice = true, // false
			initialSlicePos = 20, // Percent
			horizontalSlice = false, // true for top to bottom comparison
			keepInPlace = true, // false. Will make “after” image 100% visible when leaving the comparison area
			showLabels = true, // false
			labelBefore = 'BEFORE', // Desired label for the before image
			labelAfter = 'AFTER', // Desired label for the after image
			alwaysShowLabels = false; // Will show labels even while not hover

		/* ========================= Init */
		var pointer = '',
			posX = 0,
			posY = 0,
			slice = null,
			handle = null,
			labels = null,
			offset = '',
			beforeElement = $(comparisonArea).find('._BA_beforeElement'),
			elementWidth = $(beforeElement).width(),
			elementHeight = $(beforeElement).height();

		if (reset){
			$(comparisonArea).removeClass('hasOverlay');
			$(comparisonArea).find('._BA_slice').remove();
			$(comparisonArea).find('._BA_handle').remove();
			$(comparisonArea).find('._BA_label').remove();
		}

		/* ========================= Get values */
		showHandle = ($(comparisonArea).attr('data-showhandle')) ? $(comparisonArea).data('showhandle') : showHandle;
		handleSize = ($(comparisonArea).attr('data-handlesize')) ? $(comparisonArea).data('handlesize') : handleSize;
		showSlice = ($(comparisonArea).attr('data-showslice')) ? $(comparisonArea).data('showslice') : showSlice;
		initialSlicePos = ($(comparisonArea).attr('data-initialslicepos')) ? $(comparisonArea).data('initialslicepos') : initialSlicePos;
		horizontalSlice = ($(comparisonArea).attr('data-horizontalslice')) ? $(comparisonArea).data('horizontalslice') : horizontalSlice;
		keepInPlace = ($(comparisonArea).attr('data-keepinplace')) ? $(comparisonArea).data('keepinplace') : keepInPlace;
		showLabels = ($(comparisonArea).attr('data-showlabels')) ? $(comparisonArea).data('showlabels') : showLabels;
		labelBefore = ($(comparisonArea).attr('data-labelbefore')) ? $(comparisonArea).data('labelbefore') : labelBefore;
		labelAfter = ($(comparisonArea).attr('data-labelafter')) ? $(comparisonArea).data('labelafter') : labelAfter;
		alwaysShowLabels = ($(comparisonArea).attr('data-alwaysshowlabels')) ? $(comparisonArea).data('alwaysshowlabels') : alwaysShowLabels;

		function getEvent(event){
			return event.originalEvent.targetTouches ? event.originalEvent.targetTouches[0] : event;
		}

		/* ========================= Allows to append only once */
		if (!$(comparisonArea).hasClass('hasOverlay')){
			if (showSlice){
				beforeElement.parent().append('<div class="_BA_slice"></div>');
				slice = $(comparisonArea).find('._BA_slice');
			}
			if (showHandle){
				beforeElement.parent().append('<div class="_BA_handle"></div>');
				handle = $(comparisonArea).find('._BA_handle');
			}
			if (showLabels){
				beforeElement.parent().append('<div class="_BA_label _BA_label-left"></div><div class="_BA_label _BA_label-right"></div>');
				labels = $(comparisonArea).find('._BA_label');
			}
		}

		if (showSlice || showHandle || showLabels){ $(comparisonArea).addClass('hasOverlay'); }
		if (horizontalSlice){ $(comparisonArea).addClass('hasHorizontalSlice'); }

		/* ========================= Slice display */
		if ((showSlice) && (slice !== null)){
			if (initialSlicePos === 0){ slice.css('display', 'none'); }
			if (!horizontalSlice){
				posX = elementWidth*initialSlicePos/100;
				slice.css('left', posX + 'px');
			} else {
				posY = elementHeight*initialSlicePos/100;
				slice.css('top', posY + 'px');
			}
		}

		/* ========================= Handle display */
		if ((showHandle) && (handle !== null)){
			handle.css({
				'width': handleSize + 'px',
				'height': handleSize + 'px',
				'border-radius': handleSize + 'px'
			});
			if (!horizontalSlice){
				posY = (elementHeight-handleSize)/2;
				handle.css({
					'margin-left': handleSize / -2 + 'px',
					'top': posY + 'px',
					'left': posX + 'px'
				});
			} else {
				posX = (elementWidth-handleSize)/2;
				handle.css({
					'margin-top': handleSize / -2 + 'px',
					'top': posY + 'px',
					'left': posX + 'px'
				});
			}
		} else {
			if (!horizontalSlice){
				posX = elementWidth*initialSlicePos/100;
			} else {
				posY = elementHeight*initialSlicePos/100;
			}
		}

		/* ========================= Labels display */
		if ((showLabels) && (labels !== null)){
			$(comparisonArea).find('._BA_label-left').html(labelBefore);
			$(comparisonArea).find('._BA_label-right').html(labelAfter);
			if (!alwaysShowLabels) {
				labels.css('display', 'none');
			}
			if (horizontalSlice && showLabels){
				labels.each(function(){
					$(this).css({ // Center labels horizontaly (other attributes are set in the stylesheet)
						'width': $(this).outerWidth(),
						'left': 0,
						'right': 0
					});
				});
			}
		}

		if (!horizontalSlice){
			beforeElement.css('clip', 'rect(auto,' + posX + 'px , auto, auto)');
		} else {
			beforeElement.css('clip', 'rect(' + posY + 'px, auto, auto, auto)');
		}

		/* ========================= Comparison starts */
		$(comparisonArea).on('mouseenter touchstart', function() {
			if (!keepInPlace) {
				if (showSlice){ slice.css('display', 'block'); }
			}
		});

		/* ========================= Comparison is running */
		$(comparisonArea).on('mousemove touchmove', function(event) {
			event.preventDefault();
			pointer = getEvent(event);
			offset = $(this).offset();
			posX = pointer.pageX - (offset.left);
			posY = pointer.pageY - (offset.top);

			if (!horizontalSlice){
				beforeElement.css('clip', 'rect(auto,' + posX + 'px, auto, auto)');
			} else {
				beforeElement.css('clip', 'rect(' + posY + 'px, auto, auto, auto)');
			}
			if ((showSlice) && (slice !== null)){
				if (!horizontalSlice){
					slice.css('left', posX + 'px');
				} else {
					slice.css('top', posY + 'px');
				}
			}
			if ((showHandle) && (handle !== null)){
				handle.css({
					'display': 'none',
					'left': posX + 'px',
					'top': posY + 'px'
				});
			}
			if ((showLabels) && (labels !== null)){ labels.css('display', 'block'); }
		});

		/* ========================= Comparison ends */
		$(comparisonArea).on('mouseleave touchend touchcancel', function() {
			if (!keepInPlace) {
				beforeElement.css('clip', 'rect(auto, 0px, auto, auto)');
				if (showSlice){ slice.css('display', 'none'); }
			} else {
				if (showHandle){ handle.css('display', 'block'); }
			}
			if ((showLabels) && (!alwaysShowLabels)){ labels.css('display', 'none'); }
		});
	//});
}

//jQuery(function($){
	$(window).on('load', function(){
		/* ========================= Detecting available comparisons */
		$('._BA_comparisonArea').each(function(){
			setupComparison(this);
		});
	});
//});