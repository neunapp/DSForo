$(function(){
  var toggleMenu = $('#togle-mov-menu');
  var toggleList = $('#togle-mov-menu-list');
  var toggleRs = $('#togle-mov-menu-rs');

  toggleMenu.on('click',function(){
    //primero menu
    if (toggleList.attr('class') === 'mov-header__menu__list__disable') {
      toggleList.removeClass('mov-header__menu__list__disable').addClass('mov-header__menu__list');
    }
    else {
      toggleList.removeClass('mov-header__menu__list').addClass('mov-header__menu__list__disable');
    }

    //segundo menu
    if (toggleRs.attr('class') === 'mov-header__rs__disable') {
      toggleRs.removeClass('mov-header__rs__disable').addClass('mov-header__rs');
    }
    else {
      toggleRs.removeClass('mov-header__rs').addClass('mov-header__rs__disable');
    }

  });
});
