package Main.Model;

import org.postgresql.Driver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Context {

    private static final String CON_STR = "jdbc:postgresql://127.0.0.1:5432/My_db";

    private static Context instance = null;
    public static synchronized Context getInstance() throws SQLException{

        if(instance == null)
            instance = new Context();
        return instance;

    }

    public Connection connection;

    private Context () throws SQLException{

        DriverManager.registerDriver(new Driver());

        this.connection = DriverManager.getConnection(CON_STR,"Java", "Ecnfk");


    }



}
