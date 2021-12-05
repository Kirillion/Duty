package Main.Model;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Faculty {

    private int id;
    private String name;

    public Faculty(int id, String name){

        this.setId(id);
        this.setName(name);

    }



    public static List<Faculty> getAll() throws SQLException {


        Context context = Context.getInstance();
        try (Statement statement = context.connection.createStatement()) {

            List<Faculty> faculties = new ArrayList<Faculty>();

            ResultSet resultSet = statement.executeQuery("SELECT id,name FROM faculties");

            while (resultSet.next()){
                faculties.add(new Faculty(resultSet.getInt("id"),
                                            resultSet.getString("name")));
            }

            return faculties;

        } catch (SQLException e) {
            e.printStackTrace();

            return Collections.emptyList();
        }




    }


    public static void setOnes(Faculty faculty) throws SQLException {
        var id = getAll().size();
        Context context = Context.getInstance();
        try(PreparedStatement statement = context.connection.prepareStatement("INSERT INTO faculties(id,name)"+"VALUES(?,?)")){

            statement.setObject(1,id);
            statement.setObject(2,faculty.name);

            statement.execute();

        }catch (SQLException e){
            e.printStackTrace();
        }

    }

    public void deleteProduct(int id) throws SQLException {


        Context context = Context.getInstance();
        try (PreparedStatement statement = context.connection.prepareStatement(
                "DELETE FROM Products WHERE id = ?")) {
            statement.setObject(1, id);
            // Выполняем запрос
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }



    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
