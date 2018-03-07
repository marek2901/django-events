$('.clickable-row').on('click', function (e) {
  var notes = $(this).data('notes');
  $("#equipementNotesModal .modal-body").html(notes);
  $('#equipementNotesModal').modal('show');
});
