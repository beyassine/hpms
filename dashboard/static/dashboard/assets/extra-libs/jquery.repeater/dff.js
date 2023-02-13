var room = 1;

function education_fields() {
  room++;
  var objTo = document.getElementById("education_fields");
  var divtest = document.createElement("div");
  divtest.setAttribute("class", "mb-3 removeclass" + room);
  var rdiv = "removeclass" + room;
  divtest.innerHTML =
    '<div class="row" ><div class="col-md-5"><div class="mb-3" ><select class="form-control "><option value="">-------</option><option value="">Article 1</option><option value="">Article 2</option><option value="">Article 3</option></select></div></div><div class="col-md-5"><div class="mb-3"><input type="text" class="form-control" id="Schoolname" name="Schoolname" placeholder="Quantité" /></div></div> <div class="col-sm-2"> <div class="form-group"> <button class="btn btn-sm btn-text text-danger" type="button" onclick="remove_education_fields(' +
    room +
    ');"> <i class="fa fa-minus"></i> </button> </div></div></form>';

  objTo.appendChild(divtest);
}

function remove_education_fields(rid) {
  $(".removeclass" + rid).remove();
}
