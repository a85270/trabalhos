<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style.css">
    <title>Apagar</title>
</head>
<body>
<header><h1>Apagar Dados</h1></header>
<?php 

include("php/config.php");
if(isset($_GET['idfrutas'])){
    $idfrutas=($_GET['idfrutas']);//está a recolher os dados do ficheiro listar
}


$l=$con->prepare("SELECT * FROM frutas WHERE idfrutas='$idfrutas'");
$l->execute();
$result = $l->get_result();
while($lista=$result->fetch_assoc()){

   // coloca os dados consultados no formulário?>
    <form  method="post" action="">
            <label for="Nome"></label>
            <input type="text" name="nome" id="idnome" value="<?php echo $lista['nome'];?>">
            <label for="Árvore"></label>
            <input type="text" name="arvore" id="idarvore" value="<?php echo $lista['arvore'];?>">
            <label for="Época"></label>
            <input type="text" name="epoca" id="idepoca" value="<?php echo $lista['epoca'];?>">
            <label for="Validade"></label>
            <input type="text" name="validade" id="idvalidade" value="<?php echo $lista['validade'];?>">
            <label for="Foto"></label>
            <input type="file" name="foto" id="idfoto" value="<?php echo $lista['foto'];?>">
            <input type="submit" name="Apagar" value="Apagar">
           
        </form>

<?php
}
if (isset($_POST['Apagar'])){
    $nome=($_POST['nome']);
    $arvore=($_POST['arvore']);
    $epoca=($_POST['epoca']);
    $validade=($_POST['validade']);
    $foto=($_POST['foto']);
   // Tem a certeza que deseja apagar?
    
    $apagar=$con->prepare("DELETE FROM frutas WHERE idfrutas=$idfrutas");
    $apagar->execute();
    if($apagar)
    {
       header("location:listar.php");
    }
}
//}

$con = null;
?>
<style>

header {
    padding: 10px;
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

form input[type="text"], form input[type="file"] {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

form input[type="submit"] {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    border: none;
    background-color: rgba(76,68,182,0.808);
    color: white;
    cursor: pointer;
}
</style>
</body>
</html>