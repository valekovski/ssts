<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/styles.css" />
    <?php
      include("db.php");
      $znanstvenikID = $_GET['znanstvenikID'];
      $query = "SELECT * FROM znanstveniki WHERE ID=$znanstvenikID;";
      $result = mysqli_query($db, $query);
      $znanstvenik = mysqli_fetch_assoc($result);
    ?>
    <title><?php echo $znanstvenik['ime']." ".$znanstvenik['priimek'] ?></title>
  </head>
  <body>
    <h2><?php echo "Citati ".$znanstvenik['ime']." ".$znanstvenik['priimek'] ?></h2>
    <?php
      $quote_num = 0;
      if (isset($_GET['quote_num'])) {
        $quote_num = $_GET['quote_num'];
      }
      $query = "SELECT * FROM citati WHERE znanstvenikID=$znanstvenikID ORDER BY ID;";
      $result = mysqli_query($db, $query);

      if ($quote_num > 0) {
        $prev_quote = intval($quote_num)-1;
        echo '<a href="citati.php?znanstvenikID='.$znanstvenikID.'&quote_num='.$prev_quote.'">';
        echo '<img src="pics/nazaj.png" />';
        echo '</a>';
      }
      
      $stevec = 0;
      while ($stevec <= $quote_num) {
        $citat = mysqli_fetch_assoc($result);
        ++$stevec;
      }

      // preberi datoteko
      $fname = "docs/".$znanstvenik['ime']."_".$znanstvenik['priimek']."/".$citat['datoteka'];
      $fp = fopen($fname, "r");
      $citat_txt = fread($fp, filesize($fname));
      fclose($fp);

      echo '<textarea cols="50" rows="10">'.$citat_txt.'</textarea>';
    
      if ($quote_num < mysqli_num_rows($result) - 1) {
        $next_quote = intval($quote_num)+1;
        echo '<a href="citati.php?znanstvenikID='.$znanstvenikID.'&quote_num='.$next_quote.'">';
        echo '<img src="pics/naprej.png" />';
        echo '</a>';
      }
    ?>

    <br />
    <br />
    <a href="index.php">Nazaj na seznam znanstvenikov</a>
  </body>
</html>