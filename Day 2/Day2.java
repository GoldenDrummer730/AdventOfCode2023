import java.util.HashMap;
import java.util.Scanner;

public class Day2 {

    public static boolean is_possible(String[] sets) {
        int red_shown = 0;
        int green_shown = 0;
        int blue_shown = 0;

        for(String game : sets){
            String[] games = game.split(",");

            for(int i = 0; i < games.length; i++){
                
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int red_total = 12;
        int green_total = 13;
        int blue_total = 14;

        HashMap<String,Integer> totals = new HashMap<>();
        totals.put("red", 12);
        totals.put("green", 13);
        totals.put("blue", 14);

        Scanner scan = new Scanner("'Day 2\\sample.txt'");

        while(scan.hasNextLine()){
            System.out.println(scan.nextLine());
        }


        scan.close();
    }
}