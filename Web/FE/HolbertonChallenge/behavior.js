document.addEventListener("DOMContentLoaded", function(event) {
    var imageElement = document.getElementById("smart_thumbnail");
    imageElement.addEventListener("click", function() {
        if (imageElement.className == "") {
            imageElement.className == "small"
        } else {
            imageElement.className == ""
        }
      });
});

