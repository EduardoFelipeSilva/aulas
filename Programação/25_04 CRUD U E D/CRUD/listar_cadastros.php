<?php include_once "header.php"; 
      INCLUDE "navbar.php";
      include_once "teste.php";
    
?>
<link rel="stylesheet" href="css/navbar.css">
<link rel="stylesheet" href="css/listar_aluno.css">


</head>
    <main>
    <h1>ola</h1>
        <table border = "1px">

    <tbody>
    <?php while($dados_db = mysqli_fetch_assoc($consulta_bd)):?>
    <thead>
    <tr>
    <th>Id</th>
    <th>Nome</th>
    <th>Email</th>
    <th>Celular</th>
    </tr>
 </thead>


        <tr>
         <td> <?php echo $dados_db['id_aluno']?> </td>
         <td> <?php echo $dados_db['nome_aluno']?> </td>
         <td> <?php echo $dados_db['email_aluno']?> </td>
         <td> <?php echo $dados_db['celular_aluno']?> </td>
         <td><a href="form_atualizar_cadastro_aluno.php?id_aluno=<?php echo $dados_db['id_aluno']?>">atualizar</a></td>
         <td><a href="excluir_cadastro_aluno.php?id_aluno=<?php echo $dados_db['id_aluno']?>">excluir</a></td>

    </tr>
    <?php endwhile; ?>
    </tbody>
    </table>

    </main>


<?php include_once "footer.php" ?>