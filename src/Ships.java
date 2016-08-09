import java.util.Scanner;

//Type 0 = Aircraft carrier (Size 5 Quantity 1),
//1 = Battleship (Size 4 Quantity 1),
//2 = Cruiser (Size 3 Quantity 1),
//3 = Destroyer (Size 2 Quantity 2),
//4 = Submarine (Size 1 Quantity 2)
//Direction 0 = Vertical, 1 = Horizontal

public class Ships {
	private int type, direction, size;	
	private String name;
	private int[] initialPos;
	Scanner userInput = new Scanner(System.in);
									   	
	public Ships(int t){               	
		this.type = t;
		this.initialPos = new int[2];
		this.createShips();			   
	}
	public void createShips(){ //Assigns size and name to ship
		if(this.type == 0){
			this.name = "Aircraft Carrier";
			this.size = 5;
		}
		else if(this.type == 1){
			this.name = "Batlleship";
			this.size = 4;
		}
		else if(this.type == 2){
			this.name = "Cruiser";
			this.size = 3;
		}
		else if(this.type == 3){
			this.name = "Destroyer";
			this.size = 2;
		}
		else if(this.type == 4){
			this.name = "Submarine";
			this.size = 1;
		}
		System.out.print(this.name + " Coord Y: ");
		this.initialPos[0] = userInput.nextInt(); //Obtains coord Y
		System.out.print(this.name + " Coord X: ");
		this.initialPos[1] = userInput.nextInt(); //Obtains coord X
		System.out.print(this.name + " Direction (0 = Vertical, 1 = Horizontal): ");
		this.direction = userInput.nextInt(); //Obtains direction
	}
	public String getName(){
		return this.name;
	}
	public int[] getInitialPos(){
		return this.initialPos;
	}
	public int getShipOrientation(){
		return this.direction;
	}
	public int getShipSize(){
		return this.size;
	}
}
