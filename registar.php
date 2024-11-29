<!DOCTYPE html>
<html lang="pt-pt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style/style.css">
    <title>Inserir na BD</title>
</head>
<body>
<header>
    <h1>Registo</h1>
</header>
    <div class="nav">
        <div class="logo">
            <a href="home.php">Logo</a>
            <a href="listar.php"><button class="btn">Listar Dados</button></a>
            <a href="registar.php"><button class="btn">Registar Dados</button></a>
        </div>
            <a href="php/logout.php"> <button class="btn">Log Out</button> </a>
    </div>

    <section>
        <form  class="form" method="post" enctype="multipart/form-data" action="registo.php">
            <br>
            <label for="Nome"></label>
            <input type="text" name="nome" id="idnome" placeholder="Nome da Fruta">
            <label for="Árvore"></label>
            <input type="text" name="arvore" id="idarvore" placeholder="Árvore">
            <label for="Época"></label>
            <input type="text" name="epoca" id="idepoca" placeholder="Época">
            <label for="Validade"></label>
            <input type="date" name="validade" id="idvalidade" placeholder="Validade">
            <br>
            <label for="Foto">Foto:</label>
            <input type="file" name="foto" id="idfoto" placeholder="Foto">
            <br>
            <input type="submit" name="Registar" value="Registar">
            <input type="reset" name="Limpar" value="Limpar">
        </form>
    </section>
    <style>
        /* Seção */
section {
    margin: 20px;
}

.form {
    display: flex;
    flex-direction: column;
}

.form input[type="text"], .form input[type="date"], .form input[type="file"] {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.form input[type="submit"], .form input[type="reset"] {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    border: none;
    background: rgba(76,68,182,0.808);
    color: white;
    cursor: pointer;
}

    </style>
</body>
</html>