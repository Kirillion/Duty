package Main.Controls;

import Main.Model.Faculty;
import Main.Model.Student;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;


import java.net.URL;
import java.sql.SQLException;
import java.util.List;
import java.util.ResourceBundle;

public class Students implements Initializable {

    private ObservableList<Student> studentsData = FXCollections.observableArrayList();

    @FXML
    TableView<Student> Table;

    @FXML
    TableColumn<Faculty, Integer> idColumn;

    @FXML
    TableColumn<Faculty, String> nameColumn;

    @FXML
    TableColumn<Faculty, String> fnameColumn;

    @FXML
    TableColumn<Faculty, String> groupColumn;

    @FXML
    TableColumn<Faculty, String> facColumn;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        initData();

        idColumn.setCellValueFactory(new PropertyValueFactory<Faculty, Integer>("id"));
        nameColumn.setCellValueFactory(new PropertyValueFactory<Faculty, String>("name"));
        fnameColumn.setCellValueFactory(new PropertyValueFactory<Faculty, String>("fname"));
        groupColumn.setCellValueFactory(new PropertyValueFactory<Faculty, String>("group"));
        facColumn.setCellValueFactory(new PropertyValueFactory<Faculty, String>("fac"));


        Table.setItems(studentsData);

    }

    private void initData(){
        try {
            List<Student> students = Student.getAll();
            for (var student: students
            ) {
                    if(student.getId_group()==1){
                        studentsData.add(student);
                    }




            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }









}