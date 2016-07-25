package players;

import grids.Grid;

public class Player{
	private String name;
	private int playerNumber;
	private Grid radar;
	private Grid field;
	
	public Player(String n, int p){
		this.name = n;
		this.playerNumber = p;
		this.assignGrids();
	}
	public void assignGrids(){
		this.radar = new Grid(this, 0);
		this.field = new Grid(this, 1);
		this.radar.printGrid();
	}
}
