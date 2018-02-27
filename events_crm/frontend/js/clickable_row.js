$('.clickable-row').on('click', function (e) {
  var notes = $(this).data('notes');
  $(".modal-body").html(notes);
  $('#equipementNotesModal').modal('show');
});
