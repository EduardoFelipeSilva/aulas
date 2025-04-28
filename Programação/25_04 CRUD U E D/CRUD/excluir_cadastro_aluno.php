<?php

include "database.php";

$id_aluno = $_GET['id_aluno'];

$sql_excluir = "DELETE FROM eduardo_Felipe_sge_aluno
WHERE eduardo_Felipe_sge_aluno.id_aluno = '$id_aluno'";

if(mysqli_query($conexao,$sql_excluir))
{
    header("location:..\CRUD\listar_cadastros.php");
}
else
{
    echo "Falha ao Deletar";
}

?>