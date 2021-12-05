package Main.Controls;

import Main.Model.Context;
import Main.Model.Faculty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;


import java.net.URI;
import java.net.URL;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.List;
import java.util.ResourceBundle;

public class Faculties implements Initializable {

    private ObservableList<Faculty> facultiesData = FXCollections.observableArrayList();

    @FXML
    TableView<Faculty> Table;

    @FXML
    TableColumn<Faculty, Integer> idColumn;

    @FXML
    TableColumn<Faculty, String> nameColumn;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        initData();

        idColumn.setCellValueFactory(new PropertyValueFactory<Faculty, Integer>("id"));
        nameColumn.setCellValueFactory(new PropertyValueFactory<Faculty, String>("name"));

        Table.setItems(facultiesData);

    }

    private void initData(){
        try {
            List<Faculty> faculties = Faculty.getAll();
            for (var faculty: faculties
                 ) {

                facultiesData.add(faculty);

            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }




    @FXML
    private void Create() throws SQLException {
        Faculty faculty = new Faculty(0,"ФАВТ");
        Faculty.setOnes( faculty);



    }

    @FXML
    private void Update(){

    }

    @FXML
    private void Delete(){

    }


}
