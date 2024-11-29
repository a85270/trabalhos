<!DOCTYPE html>
<html lang="pt-pt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style.css">
    <title>Listar todos os dados</title>
</head>
<body>
<header>
        <h1>Listar os dados dos Clientes</h1>
    </header>
    <div class="nav">
        <div class="logo">
            <a href="home.php">Logo</a>
            <a href="listar.php"><button class="btn">Listar Dados</button></a>
            <a href="registar.php"><button class="btn">Registar Dados</button></a>
        </div>
            <a href="php/logout.php"> <button class="btn">Log Out</button> </a>


    </div>
<?php
        include("php/config.php");

        $listagem=$con->prepare("SELECT * FROM frutas");
        $listagem->execute();
        $result = $listagem->get_result();
        while($lista=$result->fetch_assoc()){
            echo "<li>".$lista['idfrutas']." ";
            echo " - ".$lista['nome']." ";
            echo " - ".$lista['arvore']." ";
            echo " - ".$lista['epoca']." ";
            echo " - ".$lista['validade']." ";
            echo " - ".$lista['foto'];
            $id=$lista['idfrutas'];

            
            //para mandar os dados através do URL para os ficheiros indicados a seguir
            ?> 
                
           <a href="alterar.php?idfrutas=<?php print($lista['idfrutas']);?>"><button class="btn">Editar</button></a> 
           <a href="apagar.php?idfrutas=<?php print($lista['idfrutas']);?>"><button class="btn">Apagar</button></a></li>
           <a href="download.php?idfrutas=<?php print($lista['idfrutas']);?>"><button class="btn">Download</button></a>
           
     <?php
     }

 //
 
 $con = null;
 ?>
    <style>
        
    </style>
</body>
</html>