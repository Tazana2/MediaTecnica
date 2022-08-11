<?php
    require 'consultas/conn.php';
    # Información del libro consultado
    $tituloLibro = $_POST['tituloLibro'];
    $estado = $_POST['estado'];


    # Realizar la consulta para saber el titulo del libro
    $query = "SELECT tituloLibro 
	            FROM libros
		            WHERE tituloLibro LIKE '%".$tituloLibro."%'";

    # Cursor
    $result = MYSQLI_QUERY($mysqli, $query);
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultados</title>
    </head>
    <body>
        <h2>Busqueda:</h2>
        <p>Consulta SQL realizada: <b><?php echo $query; ?></b></p>
        <table border="1">
            <tr>
                <td>T&iacute;tulo del (los) libro(s)</td>
                <td>Cantidad de ejemplares con el estado requerido</td>
            </tr>
            <tr>
                <td>
                    <?php
                        while($datos = MYSQLI_FETCH_ASSOC($result)){
                            echo "- ".$datos['tituloLibro']."<br>";
                        } 
                    ?>
                </td>
                <td>
                    <?php
                        $query = "SELECT "."COUNT(codigoEjemplar)".
                                    "FROM ejemplares
                                        WHERE estadoEjemplar = '".$estado."'";
                        $result = MYSQLI_QUERY($mysqli, $query);
                        while($datos = MYSQLI_FETCH_ROW($result)){
                            echo "- ".$datos[0]."<br>";
                        }
                    ?>
                </td>
            </tr>
        </table>
        <br>
        <h2>Informaci&oacute;n general de los libros en la biblioteca</h2>
        <table border="1">
            <tr>
                <td><b>T&iacute;tulo del libro</b></td>
                <td><b>ISBN</b></td>
                <td><b>A&ntilde;o de publicaci&oacute;n</b></td>
            </tr>
            <?php
                $query = "SELECT * FROM libros";
                $result = MYSQLI_QUERY($mysqli, $query);
                while($datos = MYSQLI_FETCH_ASSOC($result)){
                    echo "<tr>
                            <td>".$datos['tituloLibro']."</td>
                            <td>".$datos['isbn']."</td>
                            <td>".$datos['anioPublicacion']."</td>
                        </tr>";
                }
            ?>
        </table>

        <p><a href="index.php">Volver</a></p>
        <?php
            mysqli_close($mysqli);
        ?>
    </body>
</html>