package players;

import java.util.Arrays;

import grids.Grid;
import ships.Ships;

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
		this.radar = new Grid(this, 0);
		this.field = new Grid(this, 1);
		this.radar.printGrid();
	}
	public void assignShips(){
		for(int s = 0; s < 7; s++){
			if(s == 4){
				playerShips[s] = new Ships(3);
			}
			else if(s >= 5){
				playerShips[s] = new Ships(4);
			}
			else{
				playerShips[s] = new Ships(s);
			}
			System.out.print(playerShips[s].getName()+" in ");
			System.out.println(Arrays.toString(playerShips[s].getInitialPos())+"\n");
		}
	}
}
