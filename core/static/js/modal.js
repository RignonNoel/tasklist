/**
 * Created by rignonnoel on 17-01-28.
 */

function initModal(idModal, idButton){
    // Get the modal
    var modal = document.getElementById(idModal);

    // Get the button that opens the modal
    var btn = document.getElementById(idButton);

    // Get the <span> element that closes the modal
    var span = modal.getElementsByClassName("modal__content__header__close")[0];

    // When the user clicks the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    };

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    };
}