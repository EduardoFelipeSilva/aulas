<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h2>informe dois números</h2>
  <form action="calcular.php" method="get">
    <label for="num1">Valor 1</label>
    <input type="number" name="num1" id="num1"><br><br>
    <label for="num2">Valor 2</label>
    <input type="number" name="num2" id="num2"><br><br>
    <label for="operacao">informe a operação matemática que deseja</label>
    <div class="">
      <select name="operacao" id="operacao">
        <option value="1">Adição</option>
        <option value="2">Subtração</option>
        <option value="3">Multiplicacão</option>
        <option value="4">Divisão</option>
      </select>
    </div><br>
    <input type="submit" value="calcular">
  </form>
</body>
</html>