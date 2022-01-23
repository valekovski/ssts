<?php
// N = 5
/*
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
*/

/*** indeksi tabele ***/
// 00 01 02 03 04
// 10 11 12 13 14
// 20 21 22 23 24
// 30 31 32 33 34
// 40 41 42 43 44

function izpisi_2d_tabelo($tabela) {
  for ($vrstica = 0; $vrstica < count($tabela); ++$vrstica) {
    for ($stolpec = 0; $stolpec < count($tabela[$vrstica]); ++$stolpec) {
      echo $tabela[$vrstica][$stolpec]." ";
    }
    echo "<br />";
  }
}

$N = 15;
$stevila = array();
for ($vrstica = 0; $vrstica < $N; ++$vrstica) {
  $stevila[$vrstica] = array();

  for ($stolpec = 0; $stolpec < $N; ++$stolpec) {
    if ($stolpec == $vrstica) {
      $stevila[$vrstica][$stolpec] = 1;
    } else {
      $stevila[$vrstica][$stolpec] = 0;
    }
  }
}


izpisi_2d_tabelo($stevila);
?>