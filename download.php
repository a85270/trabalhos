<?php
include("php/config.php");

if (isset($_GET['idfrutas'])) {
    $idfrutas = $_GET['idfrutas'];
    $query = "SELECT foto FROM frutas WHERE idfrutas = ?";
    $stmt = $con->prepare($query);
    $stmt->bind_param("i", $idfrutas);
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();

    $foto = $row['foto'];
    $nome_foto = "foto_" . $idfrutas . ".jpg"; // você pode personalizar o nome do arquivo

    header("Content-Type: image/jpeg");
    header("Content-Disposition: attachment; filename=\"" . $nome_foto . "\"");
    echo $foto;
    exit;
}

$con = null;
?>