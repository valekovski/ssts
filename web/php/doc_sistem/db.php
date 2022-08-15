<?php
  $db = mysqli_connect("localhost", "root", "", "znanost");
  if (mysqli_error($db)) {
    die("Povezava na DB ni uspela.");
  }
?>