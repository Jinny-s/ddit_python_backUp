package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main5 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			TextField tfUser = (TextField) scene.lookup("#tfUser");
			TextField tfCom = (TextField) scene.lookup("#tfCom");
			TextField tfResult = (TextField) scene.lookup("#tfResult");
			Button btn = (Button) scene.lookup("#btn");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					String com = "";
					String result = "";
					
					double rand = Math.random();
					if(rand < 0.5) {
						com = "Ȧ";
					} else {
						com = "¦";
					}
					
					if(tfUser.getText().equals(com)) {
						result = "USER WIN!";
					} else {
						result = "USER LOSE!";
					}
					
					tfCom.setText(com);
					tfResult.setText(result);
				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
