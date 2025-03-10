<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cargo</title>
</head>
<body>
    <form action="cargo.php" method="GET">
        <label for="cargo">Selecione o Codigo do cargo para saber qual é o codigo</label><br><br>
        <div class="">
            <select name="cargo" id="cargo">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select>
        </div><br><br>
        <input type="submit" name="enviar">
    </form>
</body>
</html>