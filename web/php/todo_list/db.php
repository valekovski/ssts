<?php
  $db = mysqli_connect("localhost", "root", "", "todo");
  if (mysqli_error($db)) {
    die("Povezava na DB ni uspela.");
  }
?>