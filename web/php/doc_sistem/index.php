<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/styles.css" />
    <title>Znanstveniki</title>
    <?php
      include("db.php");
    ?>
  </head>
  <body>
    <h2>Znanstveniki</h2>
    <table>
      <?php
        $query = "SELECT * FROM znanstveniki;";
        $result = mysqli_query($db, $query);

        while ($row = mysqli_fetch_assoc($result)) {
          echo "<tr><td>";
          echo '<a href="citati.php?znanstvenikID='.$row['ID'].'">';
          echo $row['ime']." ".$row['priimek'];
          echo '</a>';
          echo "</td></tr>";
        }
      ?>
    </table>
  </body>
</html>