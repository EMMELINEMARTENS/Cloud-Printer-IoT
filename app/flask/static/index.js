window.onload = function() {
    var gadget = new cloudprint.Gadget();

    gadget.setPrintButton(
        cloudprint.Gadget.createDefaultPrintButton("print_button_container")); // div id to contain the button
    gadget.setPrintDocument("[document mimetype]", "[document title]", "[document content]", "[encoding] (optional)");
  }

  const file = document.getElementById('file');
  console.log(file.value);