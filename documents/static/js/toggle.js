$(document).ready(function(){
  var button = $(document).find('[data="toggle"]');

  button.click(function (b) {
    var x = $(b.currentTarget).parent()[0].lastElementChild;
    console.dir(b)
    $(x).slideToggle("normal");
  });
});
