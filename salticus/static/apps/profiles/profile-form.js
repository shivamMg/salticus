$(document).ready(function () {
  $("#id_profile_photo").change(function () {
    if (this.files && this.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        var img = $("<img/>")
          .attr("class", "ui fluid image")
          .attr("src", e.target.result)
          .load(function () {
            /*
            // Validate Profile Photo
            var width = this.naturalWidth;
            var height = this.naturalHeight;

            if (width !== height) {
              alert("Use a square image");
              $("#id_profile_photo").val("");
              return;
            }
            if (width < 300 || height < 300) {
              alert("Submit an image with at least 300x300 pixels resolution");
              $("#id_profile_photo").val("");
              return;
            }
            */
            $("#profile_photo_preview").html(img);
          });
      };

      reader.readAsDataURL(this.files[0]);
    }
  });
});