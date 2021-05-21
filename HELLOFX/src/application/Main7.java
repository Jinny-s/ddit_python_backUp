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


public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = FXMLLoader.load(getClass().getResource("main7.fxml"));
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
					double rand = Math.random();
					String user = tfUser.getText();
					String com = "";
					String result = "";
					
					if(rand < 0.33) {
						com = "가위";
					} else if(rand < 0.66) {
						com = "바위";
					} else {
						com = "보";
					}
					
					if(user.equals(com)) {
						result = "DRAW!";
					} else if((user.equals("가위") && (com.equals("보")))
							|| (user.equals("바위") && (com.equals("가위")))
							|| (user.equals("보") && (com.equals("바위")))) {
						result = "USER WIN!";
					} else {
						result = "UESR LOSE!";
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
