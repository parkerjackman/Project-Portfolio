// Program by Parker Jackman
import java.util.Scanner;

public class ISBN {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first 9 digits of an ISBN: ");
        int isbn9 = input.nextInt();

        int d9 = isbn9 % 10;
        int d8 = (isbn9 / 10) % 10;
        int d7 = (isbn9 / 100) % 10;
        int d6 = (isbn9 / 1000) % 10;
        int d5 = (isbn9 / 10000) % 10;
        int d4 = (isbn9 / 100000) % 10;
        int d3 = (isbn9 / 1000000) % 10;
        int d2 = (isbn9 / 10000000) % 10;
        int d1 = (isbn9 / 100000000) % 10;

        int checkSum = (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11;

        if (checkSum == 10) {
            System.out.println("The ISBN-10 number is: " + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + "X");
        }
        else {
            System.out.println("The ISBN-10 number is: " + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + checkSum);
        }
    }
}