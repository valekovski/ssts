<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/styles.css" />
    <title>TODO list</title>
    <?php
      include("db.php");

      $query = 'SELECT * FROM uporabniki WHERE username="coha"';
      $result = mysqli_query($db, $query);

      $user = mysqli_fetch_assoc($result);
      $userID = $user["id"];
    ?>
  </head>
  <body>
    <?php
      if (isset($_POST["novo_opravilo"]) && !empty($_POST["novo_opravilo"])) {
        $opravilo_opis = $_POST["novo_opravilo"];
        $query = 'INSERT INTO opravila (opis, opravljeno, userID) VALUES ("'.$opravilo_opis.'", 0, '.$userID.');';

        mysqli_query($db, $query);
      }
    ?>
    <h2>TODO list</h2>
    <form method="POST">
      <?php
        // $sql = "INSERT INTO opravila (opis, opravljeno, userID) VALUES ";
        // for ($i = 1; $i <= 33; ++$i) {
        //   $sql .= '("uči se za popravni izpit", 0, '.$i.'), ';
        //   $sql .= '("telovadi vsaj 30 min", 0, '.$i.'), ';
        // }

        // echo $sql;

        $query = 'SELECT opravila.id, opis, opravljeno, userID FROM opravila, uporabniki WHERE opravila.userID=uporabniki.id AND username="coha" AND opravljeno=0 ORDER BY opravila.id;';
        $result = mysqli_query($db, $query);

        $opravilo_num = 0;
        while ($opravilo = mysqli_fetch_assoc($result)) {
          if (isset($_POST["opravljeno".$opravilo_num])) {
            $opraviloID = $_POST["opravljeno".$opravilo_num];

            $query = "UPDATE opravila SET opravljeno=1 WHERE id=$opraviloID;";
            mysqli_query($db, $query);
          } else {
      ?>
            <input type="checkbox" class="opravljeno" name="opravljeno<?= $opravilo_num ?>" value="<?= $opravilo["id"] ?>" />
            <p class="opravilo neopravljeno_opravilo"><?= $opravilo["opis"] ?></p ><br />
      <?php
          }

          ++$opravilo_num;
        }
      ?>
      <input type="text" name="novo_opravilo" id="novo_opravilo" placeholder="Novo opravilo" />


      <br />
      <br />
      <input type="submit" id="posodobi" value="Posodobi" />
    </form>

    <br />
    <br />
    <br />
    <h3>Arhiv opravil</h3>
    <ul>
    <?php
      $query = 'SELECT * FROM opravila, uporabniki WHERE opravila.userID=uporabniki.id AND username="coha" AND opravljeno=1 ORDER BY opravila.id;';
      $result = mysqli_query($db, $query);

      while ($opravilo = mysqli_fetch_assoc($result)) {
    ?>
        <li class="opravilo opravljeno_opravilo"><?= $opravilo["opis"] ?></li>
    <?php
      }
    ?>
    </ul>
  </body>
</html>