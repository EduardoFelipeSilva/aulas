<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospedagem</title>
</head>
<body>
    <form action="hospede.php" method="GET">
        <label for="nome">Escreva o nome do hospede:</label><br><br>
        <input type="text" name="nome"><br><br>
        <label for="apartamento">Tipo de apartamento:</label><br><br>
        <div class="">
            <select name="apartamento" id="apartamento">
                <option value="Tipo A">tipo A</option>
                <option value="Tipo B">tipo B</option>
                <option value="Tipo C">tipo C</option>
                <option value="Tipo D">tipo D</option>
            </select>
        </div><br><br>
        <label for="diarias">Numero de diárias:</label><br><br>
        <input type="number" name="diaria"><br><br>
        <label for="consumo">Consumo interno:</label><br><br>
        <input type="number" step="0.1" name="consumo"><br><br>
        <input type="submit" name="enviar">
    </form>
</body>
</html>