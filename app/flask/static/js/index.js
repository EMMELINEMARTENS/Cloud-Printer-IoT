const file = document.getElementById('file');

const file_name = document.getElementById('file_name');

const file_upload = document.querySelector('.file_upload');
file_upload.addEventListener('click', (e) => {
  if(file){
    file.click();
    
    console.log(file.value); 
    console.log(file_name.value);
    file_name.innerText = file.value;
  }
},false);
window.onload = function() {

  var gadget = new cloudprint.Gadget();
  gadget.setPrintButton(
      cloudprint.Gadget.createDefaultPrintButton("print_button_container")); // div id to contain the button
  gadget.setPrintDocument("[file.value]", "[document title]", "[document content]", "[encoding] (optional)");
}
