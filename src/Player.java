import java.util.Arrays;

public class Player{
	private String name;
	private int playerNo;
	private Grid radar;
	private Grid field;
	private Ships[] playerShips;
	
	public Player(String n, int p){
		this.name = n;
		this.playerNo = p;
		this.playerShips = new Ships[7];
		this.assignGrids();
		this.assignShips();
	}
	public void assignGrids(){
		this.radar = new Grid(this, 0); //Creates radar
		this.field = new Grid(this, 1); //Creates field for own ships
	}
	public void assignShips(){ //Creates complete fleet
		for(int s = 0; s < 7; s++){
			if(s == 4){
				this.playerShips[s] = new Ships(3); //2 two sized ships
			}
			else if(s >= 5){
				this.playerShips[s] = new Ships(4); //2 one sized ships
			}
			else{
				this.playerShips[s] = new Ships(s); //Rest of ships
			}
			System.out.print(this.playerShips[s].getName()+" in "); //Prints the name and coordinates of the ship
			System.out.println(Arrays.toString(this.playerShips[s].getInitialPos())+"\n");
			
			Boolean t = this.field.lookForShips(this.playerShips[s]);
			if(t == false){
				System.out.println("Problem while assigning ship. Repeat coords");
				s--;
			}
			else{
				this.field.addShip(this.playerShips[s]);
			}
			this.field.printGrid();
		}
		
	}
}
