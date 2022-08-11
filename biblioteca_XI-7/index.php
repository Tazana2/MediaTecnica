<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Biblioteca INEM</title>
    </head>
    <body>
        <h1>Biblioteca INEM José Félix de Restrepo</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab provident vitae reiciendis odio accusantium officia ipsa consequuntur porro delectus aliquid adipisci, voluptates illum, dolorem eius dolores at excepturi error? Earum cupiditate blanditiis natus dolorum labore modi error ullam odio vel. Reprehenderit autem accusantium, esse dicta accusamus corrupti quas sequi cum! Lorem ipsum dolor sit amet consectetur adipisicing elit. Labore assumenda, iste perferendis repudiandae minus iusto necessitatibus reprehenderit voluptate quae laboriosam, quasi accusantium eaque nisi. Et voluptatum similique, officia commodi maiores consequatur quod rerum ratione asperiores, animi omnis ipsam optio accusantium beatae quisquam expedita sapiente repellendus
        </p>

        <p>blanditiis neque dicta sint iusto iure saepe soluta! Repellendus omnis, recusandae pariatur, eligendi minus repudiandae qui laudantium dolor sapiente commodi consequuntur fugit incidunt nulla dolorum aliquam corrupti impedit a, voluptatum molestias eum optio ducimus. Labore, quod architecto harum sapiente error voluptates odit itaque voluptas id quo nisi fuga quam enim officiis omnis explicabo quasi. Laudantium? Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas facilis maiores culpa quasi amet excepturi delectus architecto ut, corporis, veritatis, molestiae autem aspernatur aut! Qui reprehenderit possimus, mollitia ratione quibusdam itaque eligendi veritatis aliquid! Eligendi doloremque vel debitis perferendis totam in tenetur est optio maiores suscipit ullam illo provident quisquam sed ipsam praesentium nemo accusantium laboriosam cupiditate repellat quam illum minus, magni non! Delectus soluta id animi possimus autem? Suscipit voluptates error consequuntur officiis iure dicta. Reprehenderit, sapiente exercitationem natus a error nihil ullam architecto quibusdam. Temporibus, iste. Ut officia illum atque optio ipsum culpa a deserunt commodi laudantium possimus?
        </p>
        <h2>Consulta de libros en la Biblioteca</h2>
        
        <form name="form1" action="resultadoConsulta.php" method="post">
            <table>
                <tr>
                    <td>Digite el título o parte del título del libro: </td>
                    <td><input type="text" name="tituloLibro" size="40" placeholder="Aqu&iacute; t&iacute;tulo Libro" required></td>
                </tr>
                <tr>
                    <td>Digite una contrase&ntilde;a</td>
                    <td><input type="password" name="pwd" size="25" placeholder="Aqu&iacute; coloque su contrase&ntilde;a"></td>
                </tr>
                <tr>
                    <td>Seleccione el estado del ejemplar:</td>
                    <td>
                        <input type="radio" name="estado" value="1" checked>Disponible<br>
                        <input type="radio" name="estado" value="2">Prestado<br>
                        <input type="radio" name="estado" value="3">En reparaci&oacute;n
                    </td>
                </tr>
                <tr>
                    <td>Seleccione el(las) &aacute;reas de estudio:</td>
                    <td>
                        <input type="checkbox" name="area1" value="1">Matem&aacute;ticas<br>
                        <input type="checkbox" name="area2" value="2">Bases de datos<br>
                        <input type="checkbox" name="area3" value="3">Programaci&oacute;n
                    </td>
                </tr>
                <tr>
                    <td>Fecha y hora de solicitud:</td>
                    <td><input type="date" name="fechaSolicitud" >&nbsp;&nbsp;<input type="time" name="horaSolicitud" ></td>
                </tr>
                <tr>
                    <td>Departamento:</td>
                    <td>
                        <select name="dpto" required>
                            <option value="1">Amazonas</option>
                            <option value="2" selected>Antioqu&iacute;a</option>
                            <option value="3">Antl&aacute;ntico</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td colspan="2"><br><center><input type="submit" name="btnConsultar" value="Consultar"></center></td>
                </tr>
            </table>
        </form>
    </body>
</html>