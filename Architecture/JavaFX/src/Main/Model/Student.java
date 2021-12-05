package Main.Model;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Student {

    private int id;
    private String name;
    private String fname;
    private int id_group;
    private int id_fac;

    public String group;
    private String fac;


    public String getGroup() {
        return group;
    }

    public String getFac() {
        return fac;
    }

    public int getId() {
        return id;
    }

    public int getId_fac() {
        return id_fac;
    }

    public int getId_group() {
        return id_group;
    }

    public String getFname() {
        return fname;
    }

    public String getName() {
        return name;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setId_fac(int id_fac) {
        this.id_fac = id_fac;
    }

    public void setId_group(int id_group) {
        this.id_group = id_group;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Student(int id, String name, String fname, int id_group, int id_fac){

        setId(id);
        setName(name);
        setFname(fname);
        setId_group(id_group);
        setId_fac(id_fac);

    }

    public static List<Student> getAll() throws SQLException {


        Context context = Context.getInstance();
        try (Statement statement = context.connection.createStatement()) {

            List<Student> students = new ArrayList<Student>();
            List<Group> groups = new ArrayList<Group>();
            List<Faculty> faculties = new ArrayList<Faculty>();

            ResultSet resultSet = statement.executeQuery("SELECT id,name,fname,group_id,facultet_id FROM students");

            while (resultSet.next()){
                students.add(new Student(resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("fname"),
                        resultSet.getInt("group_id"),
                        resultSet.getInt("facultet_id")));

            }

            resultSet = statement.executeQuery("SELECT id,name FROM groups ");

            while (resultSet.next()){
                groups.add(new Group(resultSet.getInt("id"),
                        resultSet.getString("name")));

            }

            resultSet = statement.executeQuery("SELECT id,name FROM faculties");

            while (resultSet.next()){
                faculties.add(new Faculty(resultSet.getInt("id"),
                        resultSet.getString("name")));
            }

            for (var student: students
                 ) {

                for (var group: groups
                     ) {

                    if(student.getId_group()==group.getId()){
                        student.group=group.getName();
                        break;
                    }
                    if(student.group==""){
                        student.group="Не найдено";
                    }
                }

                for (var facultet: faculties
                     ) {

                    if(facultet.getId()==student.getId_fac()){
                        student.fac = facultet.getName();
                        break;
                    }

                    if(student.fac==""){
                        student.fac="Не найдено";
                    }

                }

            }

            return students;

        } catch (SQLException e) {
            e.printStackTrace();

            return Collections.emptyList();
        }




    }


}
