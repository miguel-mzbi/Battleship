package grids;

import players.Player;

public class Grid{
	private String[][] board;
	private char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
	
	public Grid(Player p, int t){
		this.createGrid();
	}
	public void createGrid(){
		this.board = new String[11][11]; //Set size of board [y][x]
		for (int r = 0; r<this.board.length;r++){
			if(r == 0){
				for (int c = 0; c <this.board.length;c++){
					if(c == 0){
						this.board[r][c] = "\\"; //00 coordinate
					}
					else{
						this.board[r][c] = String.valueOf(c); //Assign number to each column
					}
				}
			}
			else{
				for (int c = 0; c <this.board.length;c++){
					if(c == 0){
						this.board[r][c] = String.valueOf(alphabet[r-1]); //Assign letter to each row
					}
					else{
						this.board[r][c] = "~"; //Assign "valor" to each cell
					}
				}
			}
		}
	}
	public void printGrid(){
		for (int r = 0; r<board.length;r++){
			   for (int c = 0; c <board[r].length;c++){
			      System.out.print("[" +board[r][c] + "]"); // Display the content of each cell
			   }
			   System.out.println();  // go to next line
			}
	}
}
