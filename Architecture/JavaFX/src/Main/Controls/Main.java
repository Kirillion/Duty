package Main.Controls;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Collections;


public class Main {


    @FXML
    private AnchorPane content_main;


    @FXML
    private void studentsForm() throws IOException {

        Stage primaryStage = (Stage) content_main.getScene().getWindow();
        primaryStage.setWidth(727);
        primaryStage.setHeight(400);
        Parent newRoot = FXMLLoader.load(getClass().getResource("../View/Students.fxml"));
        primaryStage.getScene().setRoot(newRoot);

    }

    @FXML
    private  void groupsForm(ActionEvent event) throws IOException {

        Stage primaryStage = (Stage) content_main.getScene().getWindow();
        primaryStage.setWidth(727);
        primaryStage.setHeight(400);
        Parent newRoot = FXMLLoader.load(getClass().getResource("../View/Groups.fxml"));
        primaryStage.getScene().setRoot(newRoot);

    }

    @FXML
    private void facultiesForm(ActionEvent event) throws IOException {

        Stage primaryStage = (Stage) content_main.getScene().getWindow();
        primaryStage.setWidth(727);
        primaryStage.setHeight(400);
        Parent newRoot = FXMLLoader.load(getClass().getResource("../View/Faculties.fxml"));
        primaryStage.getScene().setRoot(newRoot);

    }

}


