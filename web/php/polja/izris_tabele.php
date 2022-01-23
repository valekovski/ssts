<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="izris_tabele.css" type="text/css" />
  </head>
  <body>
    <h1>Tabela</h1>
    <?php
      function tabela($stolpci_num, $vrstice_num) {
        for ($vrstica = 0; $vrstica < $vrstice_num; ++$vrstica) {
          for ($stolpec = 0; $stolpec < $stolpci_num; ++$stolpec) {
            $jeBelo = true;
            if (($vrstica % 2) != ($stolpec % 2)) {
              $jeBelo = false;
            }

            if ($jeBelo) {
              echo '<div class="kvadratek bel"></div>';
            } else {
              echo '<div class="kvadratek crn"></div>';
            }
          }
          echo '<br />';
        }
      }

      tabela(11, 10);
    ?>
  </body>
</html>