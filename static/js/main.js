$(document).ready(function (e) {
  // var CurrentYear = new Date().getFullYear();
  // document.getElementById('date').innerText = CurrentYear;

  $(document).bind("contextmenu",function(e) {
    return false;
  });
});

function Fid(idv){if(document.getElementById(idv)===null){throw "Error:\n  Unable to find element with id '"+idv+"'"}else{return document.getElementById(idv);}}

function snackbar(Notification) {var x = document.getElementById("snackbar");x.innerHTML=Notification;x.className = "show";setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);}

