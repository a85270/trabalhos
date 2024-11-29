<!DOCTYPE html>
<html lang="pt-pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style.css">
    <title>Document</title>
</head>
<body>
<?php
        include("php/config.php");
         //valores do formulário
        $nome=addslashes($_POST['nome']);
        $arvore=addslashes($_POST['arvore']);
        $epoca=addslashes($_POST['epoca']);
        $validade=addslashes($_POST['validade']);
        $foto=addslashes($_POST['foto']);
      
        if(isset($_POST["Registar"])){
            $query = $con->prepare("INSERT INTO frutas (nome, arvore, epoca, validade, foto) VALUES ('$nome', '$arvore', '$epoca', '$validade', '$foto')");
            $query->execute();
            if($query){
                echo"Registo efetuado com sucesso";
           }
        }
            $con = null;

    ?>
    <a href="listar.php"><button class="btn">Voltar</button></a>
</body>
</html>