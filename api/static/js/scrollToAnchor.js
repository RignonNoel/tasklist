function scrollToAnchor(aid){
    var aTag = $("#"+aid);
    $('html,body').animate({scrollTop: aTag.offset().top-50},'slow');
}